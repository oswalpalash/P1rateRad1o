from django.shortcuts import render
from django.http import HttpResponse
from .pocsag import encodeTXBatch
from .models import Device

# Create your views here.


def page(request,capcode):
    msgs = []
    user = Device.objects.get(capcode=capcode)
    msgs.append([False, user.capcode, "HELLO WORLD " + user.nick])
    data = encodeTXBatch(msgs)
    # TODO CALL FUNCTION TO ACTUALLY PAGE _data_
    return HttpResponse(data)

def index(request):
    return HttpResponse('PirateRadio')

def page_all(request):
    msgs = []
    users = Device.objects.all()
    for user in users:
      msgs.append([False, user.capcode, "HELLO WORLD " + user.nick])
      data = encodeTXBatch(msgs)
      # TODO CALL FUNCTION TO ACTUALLY PAGE _data_
    print('PAGED ALL DEVICES')
    return HttpResponse(data)
