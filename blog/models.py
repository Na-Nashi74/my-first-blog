from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='投稿者')
    title = models.CharField(max_length=200,verbose_name='タイトル')
    text = models.TextField(verbose_name='本文')
    created_date = models.DateTimeField(default=timezone.now,verbose_name='作成日')
    published_date = models.DateTimeField(blank=True, null=True,verbose_name='投稿日')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title