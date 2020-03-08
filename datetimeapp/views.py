from django.shortcuts import render
from django.http.response import HttpResponse

import datetime


def dateview(request):
    date1 = datetime.datetime.now()
    x="The current time and date is {}".format(date1)
    return HttpResponse(x)
