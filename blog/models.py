from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 올린 날짜를 자동으로 수정해 줌

    def __str__(self):
        return self.title