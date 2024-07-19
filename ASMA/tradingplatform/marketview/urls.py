from django.urls import path,re_path
from marketview import views

app_name = 'marketview'

urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    # path('newstopic/',views.news_topic,name='news_topic'),
    path('news/',views.news,name='news'),
    path('foreign_market/',views.foreign_market,name='foreign'),
    path('search/',views.search,name='search')
]