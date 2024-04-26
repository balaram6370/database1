from django.shortcuts import render

from django.http import HttpResponse

from app.models import *
# Create your views here.

def Insert_topic(request):
    tn=input('enter topic name::')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    return HttpResponse('topic created sucessfully ')

def Insert_webpage(request):
    tn=input('enter a topic name::')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter a name::')
    u=input('enter a url::')


    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    return HttpResponse('webpage created sucessfully ')


def Insert_accessrecord(request):

    tn=input('enter topic name::')

    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()

    n=input('enter a name::')
    u=input('enter a url::')

    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()

    d=input('enter a date::')
    a=input('enter a author::')

    AO=AcessRecord.objects.get_or_create(name=WO,data=d,author=a)[0]

    AO.save()

    return HttpResponse('accessrecord created sucessfully ')





