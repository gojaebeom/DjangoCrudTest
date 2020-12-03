from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False) # 제목
    writer = models.CharField(max_length=50, null=False) # 글쓴이
    content = models.TextField(null=False) # 내용
