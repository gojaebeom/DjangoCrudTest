from django.contrib import admin

# Register your models here.
from postApp.models import Post

# admin 계정에서 Post 모델을 관리해줍니다.
admin.site.register(Post)
