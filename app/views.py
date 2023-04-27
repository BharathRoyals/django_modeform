from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
def insert_Topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is inserted successfully')
    return render(request,'insert_Topic.html',d)

def insert_Webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WPFO=WebpageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('Webpage is inserted successfully')
    return render(request,'insert_Webpage.html',d)


def insert_AccessRecord(request):
    AFO=AccessRecordForm()
    d={'AFO':AFO}

    if request.method=='POST':
        ARFO=AccessRecordForm(request.POST)
        if ARFO.is_valid():
            ARFO.save()
            return HttpResponse('AccessRecord is inserted successfully')
    return render(request,'insert_AccessRecord.html',d)




