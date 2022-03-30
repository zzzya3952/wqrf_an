from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
import json


def get_devices(request):
    datas = {"errCode": 300, "Msg": "", "data": [{"name": "xiaomi", "pla": "7.9"},
                                                 {"name": "huawei", "pla": "12.9"}]}
    return HttpResponse(json.dumps(datas), content_type='application/json')
