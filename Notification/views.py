# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from forms import FilesForm
from models import Files
# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def first(request):
    # context = {}
    # if request.method == 'POST':
    form = FilesForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    print form.errors
    context = {
        'f': form,
    }
    return render(request, 'index.html', context)


@csrf_exempt
def second(request):
    from simplepush import send_user_notification
    from simplepush.models import SubscriptionInfo
    from simplepush.models import PushInformation

    user = request.user
    print user
    qry = Files.objects.all()
    payload = {"head": "Hello World", "body": "You have notification", "icon": "http://loremflickr.com/320/240",
               "link": "https://github.com/subhajeet2107/django-simplepush"}
    send_user_notification(user=user, payload=payload, ttl=10000)
    # print SubscriptionInfo.objects.all()
    # print PushInformation.objects.all()
    return render(request, 'simplepush_message.html', {})
