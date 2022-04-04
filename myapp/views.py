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


def upload_env_script(request):
    # 接收上传的这个文件-环境脚本
    myFile = request.FILES.get('upload_env_script', None)
    # 判断接收的是否为空
    if myFile == None:
        return HttpResponse('未选择任何本地文件！')
    else:  # 说明有内容
        fileName = str(myFile)  # 文件名拿到
        fp = open('scripts/env/' + fileName, 'wb+')
        for i in myFile.chunks():
            fp.write(i)
        fp.close()
        # 更改数据库
        DB_env_script.objects.all().update(script=fileName)
        return HttpResponseRedirect('/index/')


# 查
def get_cases(request):
    cases = list(DB_cases.objects.all().values())
    res = {"cases": cases}
    return HttpResponse(json.dumps(res), content_type='application/json')


# 增
def add_cases(request):
    DB_cases.objects.create()
    return get_cases(request)


# 删
def del_cases(request):
    case_id = request.GET['case_id']
    DB_cases.objects.filter(id=case_id).delete()
    return get_cases(request)


# 改
def save_cases(request):
    case_id = request.GET['case_id']
    new_name = request.GET['new_name']
    new_level = request.GET['new_level']
    new_ifut = request.GET['new_ifut']
    new_ifut = False if new_ifut == 'false' else True
    DB_cases.objects.filter(id=case_id).update(name=new_name, level=new_level, ifut=new_ifut)
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


# 获取数据变量
def get_datas(request):
    datas = list(DB_datas.objects.all().values())  # 此时它才是 [{},{}]
    res = {"datas": datas}
    return HttpResponse(json.dumps(res), content_type='application/json')



# 增加数据变量
def add_datas(request):
    DB_datas.objects.create()

    return get_datas(request)


# 删除数据变量
def del_datas(request):
    id = request.GET['id']
    DB_datas.objects.filter(id=id).delete()
    return get_datas(request)


# 修改数据变量
def save_datas(request):
    id = request.GET['id']
    new_name = request.GET['new_name']
    new_value = request.GET['new_value']
    DB_datas.objects.filter(id=id).update(name=new_name, value=new_value)
    return get_datas(request)

