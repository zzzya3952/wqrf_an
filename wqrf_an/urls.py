"""wqrf_an URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from myapp.views import *
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_devices/', get_devices),
    path('index/', TemplateView.as_view(template_name='index.html')),
    path('get_env_script/', get_env_script),
    path('upload_env_script/', upload_env_script),
    path('get_cases/', get_cases),
    path('add_cases/', add_cases),
    path('del_cases/', del_cases),
    path('save_cases/', save_cases),
    re_path('upload_case/(?P<case_id>.+)/', upload_case),

    path('get_datas/', get_datas),
    path('add_datas/', add_datas),
    path('del_datas/', del_datas),
    path('save_datas/', save_datas),
]
