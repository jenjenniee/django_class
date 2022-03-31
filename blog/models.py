from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) #현재시간 자동 저장
    updated_at = models.DateTimeField(auto_now=True) #다시 저장 할 때마다 그 시간이 저장되게 함

    def __str__(self):
        # 브라우저 및 어드민에 보이는 형식
        return f'[{self.pk}] {self.title}'

    #author :  추후작성예정
