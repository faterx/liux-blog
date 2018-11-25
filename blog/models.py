from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): # 定义一个对象
    # 指向另一个模型的连接
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    # 如何用为数有限的字符来定义一个文本。
    title = models.CharField(max_length=200)
    # 没有长度限制的长文本
    text = models.TextField()
    created_date = models.DateField(default=timezone.now)
    # 时间和日期
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title