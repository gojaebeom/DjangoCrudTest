from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False) # 제목
    content = models.TextField(null=False) # 내용
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 외래키 설정

