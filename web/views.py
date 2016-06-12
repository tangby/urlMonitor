#coding:utf-8
from django.shortcuts import render, render_to_response
import threading,datetime
from web.models import items
from vo import monitor
from utils import getThread,stopMonitor,startMonitor,getLogger,createMonitor,getMonitorById,modifyMonitor
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    #monitors = threading.enumerate()
    #monitors=getThread(monitors)
    #monitors=['1','2','a','b']
    monitors=getThread()
    for i in monitors:
        print type(i.smsBegin)
        print i.smsBegin
        print 'get get-------' + str(i.mName)
    return render_to_response('index.html',{'monitors':monitors})

def stop(request):
    id=int(request.GET.get('id'))
    #通过id查找到对应的monitor thread对象，并修改它的status属性为False
    if stopMonitor(id):
        #从数据库里把对应的记录status字段修改为False
        item=items.objects.get(id=id)
        print 'debug stop'+str(item.name)
        item.status=False
        item.save()
        #修改后跳转到首页
        return HttpResponseRedirect('/index/')
    #通过id无法查询到的时候返回
    return HttpResponse('id is not exisit')

def start(request):
    id=int(request.GET.get('id'))
    if startMonitor(id):
        item=items.objects.get(id=id)
        print 'debug stop'+str(item.name)
        item.status=True
        item.save()
        return HttpResponseRedirect('/index/')
    return HttpResponse('id is not exisit')

def add(request):
    if request.method == 'GET':
        return render_to_response('add.html')
    else:
        m=createMonitor(
            log=getLogger(),
            name=request.POST.get('name'),
            interval=request.POST.get('interval'),
            mailInterval=request.POST.get('mailInterval'),
            smsInterval=request.POST.get('smsInterval'),
            smsBegin=request.POST.get('smsBegin'),
            smsEnd=request.POST.get('smsEnd'),
            retryTimes=request.POST.get('retryTimes'),
            retryInterval=request.POST.get('retryInterval'),
            describe=request.POST.get('describe'),
            url=request.POST.get('url'),
            timeout=request.POST.get('timeout'),
            contacts=request.POST.get('contacts'),
            statusCode=request.POST.get('statusCode'),
            status=False,
        )
        if m:
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse('create failed')
        
def deleteMonitor(request):
    id=request.GET.get('id')
    m=getMonitorById(id)
    if m:
        m.stop()
        items.objects.filter(id=id).delete()
        return HttpResponseRedirect('/index/')
    else:
        return HttpResponse('can not find ')
    
def modify(request):
    if request.method == 'GET':
        id=request.GET.get('id')
        m=getMonitorById(id)
        if m:
            #sb=str(m.smsBegin)
            #se=str(m.smsEnd)
            return render_to_response('modify.html',{'monitor':m})
        else:
            return HttpResponse('id is not exisit')
    else:
        m=modifyMonitor(
            oldName=request.POST.get('oldName'),
            log=getLogger(),
            name=request.POST.get('name'),
            interval=request.POST.get('interval'),
            mailInterval=request.POST.get('mailInterval'),
            smsInterval=request.POST.get('smsInterval'),
            smsBegin=request.POST.get('smsBegin'),
            smsEnd=request.POST.get('smsEnd'),
            retryTimes=request.POST.get('retryTimes'),
            retryInterval=request.POST.get('retryInterval'),
            describe=request.POST.get('describe'),
            url=request.POST.get('url'),
            timeout=request.POST.get('timeout'),
            contacts=request.POST.get('contacts'),
            statusCode=request.POST.get('statusCode'),
            status=False,
        )
        if m:
            return HttpResponseRedirect('/index/')
        else:
            return HttpResponse('modify failed')
        