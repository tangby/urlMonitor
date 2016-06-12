#!/usr/bin/env python
#coding:utf-8
from threading import Thread
import time
import requests
import datetime
class monitor(Thread):
    
    def __init__(self,**args):
        self.work=True
        self.id=args['id']
        self.log=args['logger']
        self.mName=args['name']
        self.interval=args['interval']
        self.mailInterval=args['mailInterval']
        self.smsInterval=args['smsInterval']
        self.smsBegin=args['smsBegin']
        self.smsEnd=args['smsEnd']
        self.retryTimes=args['retryTimes']
        self.describe=args['describe']
        self.url=args['url']
        self.timeout=args['timeout']
        self.retryInterval=args['retryInterval']
        self.contacts=args['contacts']
        self.status=args['status']
        self.statusCode=args['statusCode']
        print self.mName,'retry interval',self.retryInterval
        super(monitor,self).__init__()
        
    def exec_monitor(self):
        print self.mName+' started'
        sleep_time=self.interval
        fail_count=0
        last_sms=time.time()
        while self.work:
            if self.status:
                print self.mName+' running'
                try:
                    result=False
                    now_time=datetime.time(hour=datetime.datetime.now().hour,minute=datetime.datetime.now().minute)
                    result=requests.get(self.url,timeout=self.timeout/1000)
                    print self.mName
                except Exception,e:
                    print e
                if result:
                    if result.status_code == self.statusCode:
                        info=self.mName+' monitor ok'
                        self.log.write(info)
                        sleep_time=self.interval
                        last_sms=time.time()
                        fail_count=0
                        sleep_time=self.interval
                    else:
                        info=self.mName+' monitor status wrong: '+str(result.status_code)
                        if fail_count >= self.retryTimes and (time.time()-last_sms)/60>= self.smsInterval and now_time > self.smsBegin and now_time < self.smsEnd:
                            self.smsNotify(info=info)
                            last_sms=time.time()
                            fail_count=0
                        else:
                            fail_count+=1
                        
                        self.mailNotify(info)
                        sleep_time=self.retryInterval
                else:
                    info=self.mName+' monitor timeout'
                    if fail_count >= self.retryTimes and (time.time()-last_sms)/60>= self.smsInterval and now_time > self.smsBegin and now_time < self.smsEnd:
                        self.smsNotify(info=info)
                        last_sms=time.time()
                        fail_count=0
                    else:
                        fail_count+=1
                    
                    self.mailNotify(info)
                    sleep_time=self.retryInterval
            else:
                pass
            #print '1',type(self.interval)
            #print '2',type(sleep_time)
            print 'sleepTime:'+str(sleep_time)
            if self.work:
                time.sleep(sleep_time)
                   
            #time.sleep(sleep_time)
        
    def smsNotify(self,info):
        self.log.write(self.mName+' notify by sms'+info)
    def mailNotify(self,info):
        self.log.write(self.mName+' notify by mail'+info)
    def stop(self):
        self.work=False
    def run(self):
        print self.mName+' start'
        self.exec_monitor()