#coding:utf-8
from __future__ import unicode_literals


from django.db import models

# Create your models here.
class items(models.Model):

    #监控名
    name = models.CharField(max_length=30)
    #监控间隔
    interval = models.IntegerField() 
    #邮件通知间隔
    mailInterval = models.IntegerField()
    #短信通知间隔
    smsInterval = models.IntegerField()
    #短信报警起始时间
    smsBegin = models.TimeField()
    #短信报警结束时间
    smsEnd = models.TimeField()
    #重试次数
    retryTimes = models.IntegerField()
    #描述
    describe = models.CharField(max_length=200)
    #url
    url = models.CharField(max_length=200)
    #超时时间
    timeout = models.IntegerField()
    #重试间隔
    retryInterval = models.IntegerField()
    #联系人
    contacts = models.CharField(max_length=30)
    #监控状态
    status = models.BooleanField()
    #返回码
    statusCode = models.IntegerField()
    