from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Contents(models.Model):
    title = models.TextField(verbose_name='제목')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='사진',null=True,blank=True)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True,blank=True)
    
class Comment(models.Model):
    content = models.TextField(verbose_name='댓글 내용')
    created_at = models.DateTimeField(verbose_name='작성일',auto_now_add=True)
    writer = models.ForeignKey(to=User,on_delete=models.CASCADE)