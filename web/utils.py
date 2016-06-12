#!/usr/bin/env python
#coding:utf-8
import sys
import time
import threading
import datetime

from web.vo import monitor

class logger():
    def __init__(self):
        logfile=sys.path[0]+'\out.log'
        self.__logfile=logfile
        self.f=open(logfile,'a+')
    def write(self,info='info is null'):
        localTime=time.strftime('%Y-%m-%d %H:%M:%S')
        if not info.endswith('\n'):
            info=info+'\n'
        self.f.write(localTime+' '+info)
        self.f.flush()

        print localTime+' '+info

#获取所有monitor类对象        
def getThread():
    monitors=[]
    objects=threading.enumerate()
    for i in objects:
        if type(i) == monitor:
            if i.work==True:
                monitors.append(i)
    return set(monitors)
#获取或生成logger对象
def getLogger():
    objects=threading.enumerate()
    for i in objects:
        if type(i) == logger:
            return i
    log = logger()
    return log
#创建一个monitor对象
def createMonitor(**args):
    from web.models import items
    m=items.objects.filter(name=args['name'])
    if m:
        return False
    else:
        log=args['log']
        print 'create ------------' + args['name']
        m=items(
            name=args['name'],
            interval=args['interval'],
            mailInterval=args['mailInterval'],
            smsInterval=args['smsInterval'],
            smsBegin=args['smsBegin'],
            smsEnd=args['smsEnd'],
            retryTimes=args['retryTimes'],
            retryInterval=args['retryInterval'],
            describe=args['describe'],
            url=args['url'],
            timeout=args['timeout'],
            contacts=args['contacts'],
            statusCode=args['statusCode'],
            status=args['status']
        )
        m.save()
        time.sleep(0.5)
        i=items.objects.filter(name=args['name'])[0]
        m=monitor(logger=log,id=i.id,name=i.name,interval=i.interval,mailInterval=i.mailInterval,smsInterval=i.smsInterval,smsBegin=i.smsBegin,smsEnd=i.smsEnd,retryTimes=i.retryTimes,describe=i.describe,url=i.url,timeout=i.timeout,retryInterval=i.retryInterval,contacts=i.contacts,status=i.status,statusCode=i.statusCode)
        m.setName(i.name)
        m.start()
        return True
#通过id停掉指定monitor        
def stopMonitor(id):
    print 'method:'+str(id)

    monitors=getThread()
    for monitor in monitors:
        if monitor.id==id:
            monitor.status=False
            print str(id)+':stopped'
            monitor.log.write(monitor.mName+' stopped')  
            return True
    return False
#通过id start 指定monitor
def startMonitor(id):
    print 'method:'+str(id)

    monitors=getThread()
    for monitor in monitors:
        if monitor.id==id:
            monitor.status=True
            print str(id)+':started'
            monitor.log.write(monitor.mName+' started')  
            return True
    return False
#通过id查找指定monitor对象
def getMonitorById(id):
    monitors=threading.enumerate()
    for i in monitors:
        if type(i) == monitor:
            if i.id == int(id):
                return i
    return False
#通过name查找指定monitor对象
def getMonitorByName(name):
    monitors=threading.enumerate()
    for i in monitors:
        if type(i) == monitor:
            if i.mName == str(name):
                return i
    return False
#修改monitor对象
def modifyMonitor(**args):
    from web.models import items
    m=getMonitorByName(name=args['oldName'])
    if m:
        print '1111'+m.mName
        m.mName=args['name']
        m.interval=args['interval']
        m.mailInterval=args['mailInterval']
        m.smsInterval=args['smsInterval']
        m.smsBegin=args['smsBegin']
        m.smsEnd=args['smsEnd']
        m.retryTimes=args['retryTimes']
        m.retryInterval=args['retryInterval']
        m.describe=args['describe']
        m.url=args['url']
        m.timeout=args['timeout']
        m.contacts=args['contacts']
        m.statusCode=args['statusCode']
        m.status=args['status']
        #更新数据库
        i=items.objects.filter(name=args['oldName'])[0]
        print 'insert into db ------------------'+str(i.name)
        print '---------------------------------'
        
        i.name=args['name']
        i.interval=args['interval']
        i.mailInterval=args['mailInterval']
        i.smsInterval=args['smsInterval']
        i.smsBegin=args['smsBegin']
        i.smsEnd=args['smsEnd']
        i.retryTimes=args['retryTimes']
        i.retryInterval=args['retryInterval']
        i.describe=args['describe']
        i.url=args['url']
        i.timeout=args['timeout']
        i.contacts=args['contacts']
        i.statusCode=args['statusCode']
        i.status=args['status']
        i.save()
        
        return True
    else:
        return False