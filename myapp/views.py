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


def get_env_script(request):
    script = DB_env_script.objects.all()[0].script
    return HttpResponse(script)


def upload_env_script(request):  # 接收上传的脚本文件--环境脚本
    myFile = request.FILES.get('upload_env_script', None)
    if myFile == None:  # 判断接收文件是否为空
        return HttpResponse('未选择任何本地文件：')
    else:  # 说明有内容
        fileName = str(myFile)  # 拿到文件名
        fp = open('Scripts/env/' + fileName, 'wb+')
        for i in myFile.chunks():
            fp.write(i)
        fp.close()
        # 更改数据库
        DB_env_script.objects.all().update(script=fileName)
        return HttpResponseRedirect('/index/')


# 查询
def get_cases(request):
    cases = list(DB_cases.objects.all().values())
    res = {"cases": cases}
    return HttpResponse(json.dumps(res), content_type='application/json')


# 增加
def add_cases(request):
    DB_cases.objects.create()
    return get_cases(request)


# 删除
def del_cases(request):
    case_id = request.GET['case_id']
    DB_cases.objects.filter(id=case_id).delete()
    return get_cases(request)


# 修改
def save_cases(request):
    case_id = request.GET['case_id']
    new_name = request.GET['new_name']
    new_level = request.GET['new_level']
    DB_cases.objects.filter(id=case_id).update(name=new_name, level=new_level)
    return get_cases(request)


# 上传用例脚本。
def upload_case(request, case_id):
    myFile = request.FILES.get('upload_case_script', None)
    if myFile == None:
        print('没有文件脚本出现')
        return HttpResponseRedirect('/index/')
    file_name = str(myFile)
    fp = open('scripts/case/' + file_name, 'wb+')
    for i in myFile.chunks():
        fp.write(i)
    fp.close()
    DB_cases.objects.filter(id=case_id).update(script=file_name)
    return HttpResponseRedirect('/index/')
