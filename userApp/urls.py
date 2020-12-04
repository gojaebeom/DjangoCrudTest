from django.urls import path

from userApp import views

urlpatterns = [
    # GET
    path('', views.user_list, name="list"),
    # GET
    path('<int:id>', views.user_detail, name="detail"),
    path('<int:id>/edit', views.user_edit, name="edit"),
    path('<int:id>/delete', views.user_delete, name="edit"),
]
