from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
import json
from myapp.models import *
import os,signal
import time
import subprocess
import shutil


def get_devices(request):
    res = {}
    datas = DB_devices.objects.all()
    res["errCode"] = 200
    res["msg"] = ""
    res["data"] = list(datas.values())
    return HttpResponse(json.dumps(res),content_type='application/json')


# 获取环境
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


# 查询用例
def get_cases(request):
    cases = list(DB_cases.objects.all().values())
    res = {"cases": cases}
    return HttpResponse(json.dumps(res), content_type='application/json')


# 增加用例
def add_cases(request):
    DB_cases.objects.create()
    in_tjs('新增用例')
    return get_cases(request)


# 删除用例
def del_cases(request):
    case_id = request.GET['case_id']
    DB_cases.objects.filter(id=case_id).delete()
    in_tjs('删除用例')
    return get_cases(request)


# 修改用例
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
    in_tjs('添加数据')
    return get_datas(request)


# 删除数据变量
def del_datas(request):
    id = request.GET['id']
    DB_datas.objects.filter(id=id).delete()
    in_tjs('删除数据')
    return get_datas(request)


# 修改数据变量
def save_datas(request):
    id = request.GET['id']
    new_name = request.GET['new_name']
    new_value = request.GET['new_value']
    DB_datas.objects.filter(id=id).update(name=new_name, value=new_value)
    return get_datas(request)


# 上传apk包
def up_apk(request):
    myFile = request.FILES.get('up_apk_name', None)
    if not myFile:
        return HttpResponse('未上传任何apk!')
    file_name = str(myFile)
    fp = open('scripts/apk/' + file_name, 'wb+')  # with open('','wb+') as fp:
    for i in myFile.chunks():
        fp.write(i)
    fp.close()
    return HttpResponse('上传成功! 当前包名为：' + file_name)


# 重新授权
def fix_device(request):
    # 删除旧的授权文件
    try:
        os.remove('/Users/wangzijia/.android/adbkey')
        os.remove('/Users/wangzijia/.android/adbkey.pub')
    except:
        pass
    # 重新启动adb
    time.sleep(1)
    subprocess.Popen('adb kill-server', shell=True)
    time.sleep(1)
    subprocess.Popen('adb devices', shell=True)
    time.sleep(2)
    return get_devices(request)


# 写入统计函数
def in_tjs(name):
    s = DB_tjs.objects.get_or_create(day=time.strftime('%y-%m-%d', time.localtime(time.time())))
    old_value = json.loads(s[0].value)  # 此时old_value是一个字典
    try:
        old_value[name] += 1
    except:
        old_value[name] = 1
    s[0].value = json.dumps(old_value)
    s[0].save()


# 获取统计数据
def get_tjs(request):
    tjs = DB_tjs.objects.all()[::-1][:30][::-1]
    res = {}
    res['legend_data'] = []  # 种类
    res['xAxis_data'] = []  # 日期
    res['series'] = []  # 具体数据 [{"name","data","type"},{},{}]
    # 重组数据
    for tj in tjs:
        res['xAxis_data'].append(tj.day)
        value = json.loads(tj.value)
        for key in value.keys():
            if key not in res['legend_data']:
                res['legend_data'].append(key)
    for i in res['legend_data']:
        tmp = {"name": i, "data": [], "type": "line"}
        for tj in tjs:
            value = json.loads(tj.value)  # value 就是 {"新增用例":5,"删除用例":2}
            if i in value.keys():  # i 是 '新增用例'
                tmp['data'].append(value[i])  # value[i] 就是 字典['新增用例'] 其实就是5
            else:
                tmp['data'].append(0)
        res['series'].append(tmp)
    return HttpResponse(json.dumps(res), content_type='application/json')


# 获取任务列表
def get_tasks(request):
    tasks = list(DB_tasks.objects.all().values())[::-1]
    res = {'tasks': tasks}
    return HttpResponse(json.dumps(res), content_type='application/json')


# 启动任务
def play(request):
    for i in request.POST.lists():
        print(i[0])

    return HttpResponse('')
