from django.db import models


# Create your models here.
class DB_devices(models.Model):
    name = models.CharField(max_length=20, default='')  # 字符串类型，最大长度20，默认值为空字符串
    pla = models.FloatField(default=0.0)  # 安卓系统版本号
    udid = models.CharField(max_length=30, default='')  # 物理设备识别码
    state = models.CharField(max_length=10, default='')  # 设备状态,空闲/使用中/未链接/授权失败

    def __str__(self):
        return self.name


class DB_env_script(models.Model):  # 存放当前正在选择的脚本名字
    script = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.script


class DB_cases(models.Model):
    name = models.CharField(max_length=30, default='')
    script = models.CharField(max_length=50, default='')
    level = models.IntegerField(default=0)
    ifut = models.BooleanField(default=True)  # 是否为unittest官方脚本

    def __str__(self):
        return self.name


class DB_datas(models.Model):
    name = models.CharField(max_length=30, default='')
    value = models.TextField(default='{}')

    def __str__(self):
        return self.name
