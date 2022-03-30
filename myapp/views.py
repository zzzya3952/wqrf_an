from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json
from myapp.models import *
import os, signal
import time
import subprocess
import shutil


def get_devices(request):
    res = {}
    datas = DB_devices.objects.all()
    res["errCode"] = 200
    res["msg"] = ""
    res["data"] = list(datas.values())
    return HttpResponse(json.dumps(res), content_type='application/json')
