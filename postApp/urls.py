from django.urls import path
from postApp import views

urlpatterns = [
    # GET /posts
    path('', views.post_list, name="index"), 
    # GET /posts/:id
    path('<int:id>', views.post_detail, name="detail"), 
    # GET, POST /posts/create
    path('create', views.post_create, name="create"), 
    # GET, PUT /posts/:id/edit
    path('<int:id>/edit', views.post_update, name="update"), 
    # DELETE /posts/:id
    path('<int:id>/delete', views.post_delete, name="delete"),
]
