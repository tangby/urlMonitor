from __future__ import unicode_literals

from django.apps import AppConfig
from vo import monitor
from utils import logger
import datetime
#from .models import items
class WebConfig(AppConfig):
    name = 'web'
    
    def ready(self):
        print '############initialization###############'
        log=logger()
        #m=monitor(log=log,name='test1',interval=10,mailInterval=10,smsInterval=30,smsBegin=1,smsEnd=1,describe=1,contacts=1,retryTimes=3,url='http://www.baidu.com',timeout=1000,retryInterval=5,status=True,statusCode=200)
        #m.start()
        from models import items
        result=items.objects.all()
        for i in result:
            m=monitor(logger=log,id=i.id,name=i.name,interval=i.interval,mailInterval=i.mailInterval,smsInterval=i.smsInterval,smsBegin=i.smsBegin,smsEnd=i.smsEnd,retryTimes=i.retryTimes,describe=i.describe,url=i.url,timeout=i.timeout,retryInterval=i.retryInterval,contacts=i.contacts,status=i.status,statusCode=i.statusCode)
            m.setName(i.name)
            m.start()
            