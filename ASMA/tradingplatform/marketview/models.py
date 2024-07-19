from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)


    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
    
# class NewsTopic(models.Model):

#     news_topics = {
#         "blockchain":"Blockchain",
#         "earnings":"Earnings",
#         "ipo":"IPO",
#         "mergers_and_acquisitions":"Mergers & Acquisitions",
#         "financial_markets":"Financial Markets",
#         "economy_macro":"Economy",
#         "energy_transportation":"Energy & Transportation",
#         "finance":"Finance",
#         "life_sciences":"Life Sciences",
#         "manufacturing":"Manufacturing",
#         "real_estate":"Real Estate & Construction",
#         "retail_wholesale":"Retail & Wholesale",
#         "technology":"Technology"
#     }
#     topic = models.CharField(max_length=30,choices=news_topics)

#     def __str__(self):
#         return self.topic
    
class NewsList(models.Model):

    title = models.CharField(max_length=256)
    thumbnail = models.ImageField(blank=True)
    date = models.DateField(auto_now=True)
    time = models.TimeField(blank=True,auto_now=True)
    source = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    link = models.URLField(max_length=256,blank=True)
    summary = models.CharField(max_length=256,default='...')

    def __str__(self):
        return self.title
    