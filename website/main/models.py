from django.db import models


# Create your models here.
class WebsiteUsers(models.Model):
    username = models.CharField('Username', max_length=120)
    email = models.CharField('Email Address', max_length=120)
    password = models.CharField('Password', max_length=120)
    city = models.CharField('City', max_length=120)
    phone = models.FloatField('Phone Number', max_length=120)


