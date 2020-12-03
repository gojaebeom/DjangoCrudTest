from django.urls import path

from signApp import views

urlpatterns = [
    # GET, POST
    path('join', views.join, name="join"),
    # GET, POST
    path('login', views.login, name="login"),
]
