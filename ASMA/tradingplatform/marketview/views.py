from django.shortcuts import render
from . import forms
from marketview.models import NewsList
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib.auth import authenticate,login,logout
import pandas_datareader.av.time_series as ts
import pandas_datareader.nasdaq_trader as nt
import pandas as pd
import requests
import json
import plotly.graph_objects as go



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        profile_form = forms.UserProfileInfoForm(request.POST)

        if form.is_valid() and profile_form.is_valid():

            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(form.errors,profile_form.errors)
    else:
        form = forms.UserForm()
        profile_form = forms.UserProfileInfoForm()

    user_dict = {'user_form':form,'profile_form':profile_form,'registered':registered}
    return render(request,'marketview/registration.html',context=user_dict)

def index(request):
    return render(request,'marketview/index.html')

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
            
        else:
            print("Someone tried to login and failed!")
            print(f"Username: {username} and password {password}")
            return HttpResponse("invalid login details supplied")
        
    else:
        return render(request,'marketview/login.html',{})
    
def news(request):

    temp = NewsList.objects.all()

    temp.delete()

    selected = False

    if request.method == 'POST':
        top = request.POST.get('topic')

        selected=True

        # top = NewsTopic.objects.get()
    
        news_dict = requests.get(f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&topics={top}&apikey=TRL8S38I56MBYQ4D").json()

        for feed in news_dict['feed']:

            tit = feed['title']
            thumb = feed['banner_image']
            d = feed['time_published'].split('T')[0]
            t = feed['time_published'].split('T')[1]
            src = feed['source']
            athr = ' '.join(feed['authors'])
            lnk = feed['url']
            smry = feed['summary']

            nslst = NewsList.objects.get_or_create(title=tit,thumbnail=thumb,date=d,time=t,source=src,author=athr,link=lnk,summary=smry)

        news_list = NewsList.objects.order_by('date')
        return render(request,'marketview/news.html',context={"news_list":news_list,"selected":selected})
    
    else:
        return render(request,'marketview/news.html',context={"selected":selected})
        
    
# def news_topic(request):


#     temp = NewsTopic.objects.all()
#     temp.delete()

#     if request.method == "POST":
#         form = forms.NewsTopicForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('marketview:news'))
#         else:
#             print(form.errors)
#     else:
#         form = forms.NewsTopicForm()
        
#     return render(request,'marketview/newstopic.html',context={"select_topic":form})

def foreign_market(request):
    # ibm = dataread.Stocks.StockFrame() 
    # fig = go.Figure(data=[go.Candlestick(x=ibm.index,
    #                                      open=ibm['open'],high=ibm['high'],
    #                                      low=ibm['low'],close=ibm['close'])
    #                                      ]).to_html()
    # context = {'fig':fig}
    # df = ts.AVTimeSeriesReader(symbols='IBM',function='TIME_SERIES_INTRADAY',start='6/20/24',end='6/21/24',api_key="TRL8S38I56MBYQ4D").read()
    
    # time = df.index
    # open = df['open']
    # high = df['high']
    # low = df['low']
    # close = df['close']

    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={sym}&interval=5minapikey=TRL8S38I56MBYQ4D'

    
    selected=True
    sym = request.GET.get('symbol')
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    r = requests.get(url)
    dat = r.json()
    times = [key for key in dat["Time Series (Daily)"].keys()]
    prices = [dat["Time Series (Daily)"][time] for time in times]
    opens = [inst['1. open'] for inst in prices]
    highs = [inst['2. high'] for inst in prices]
    lows = [inst['3. low'] for inst in prices]
    closes = [inst['4. close'] for inst in prices]
    
    return render(request,'marketview/foreign_markets.html',{"times":json.dumps(times),"opens":json.dumps(opens),"highs":json.dumps(highs),"lows":json.dumps(lows),"closes":json.dumps(closes),"selected":selected})

    
def search(request):
    
    if request.method == 'GET':
        key = request.GET.get('symbol')
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={key}&apikey=TRL8S38I56MBYQ4D'
        data = requests.get(url).json()
        symbols = [item["1. symbol"] for item in data["bestMatches"]]
        return JsonResponse({ "data": symbols})
        