"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls.conf import include

from postApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('postApp.urls')),  # 생성한 postApp 폴더 내의 urls.py를 참조
    path('users/', include('userApp.urls')),  # user 경로
    path('account/', include('allauth.urls')),  # oauth에 필요한 url
    path('', views.post_list),  # default home
    path('', include('signApp.urls')),  # signApp의 url.py를 참조
]
