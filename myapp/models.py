from django.db import models

# Create your models here.
class DB_devices(models.Model):
    name = models.CharField(max_length=20,default='')  #字符串类型，最大长度20，默认值为空字符串
    pla = models.FloatField(default=0.0) #安卓系统版本号
    udid = models.CharField(max_length=30,default='') #物理设备识别码
    state = models.CharField(max_length=10,default='') #设备状态,空闲/使用中/未链接/授权失败
    def __str__(self):
        return self.name
