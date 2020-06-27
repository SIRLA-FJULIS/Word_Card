from django.conf import settings
from django.db import models
from django.utils import timezone
from account.models import User #打勾功能引入需要
# Create your models here.
class Set(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    set_name = models.CharField(max_length=128, unique=True)#單字集的名稱
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.set_name



class Word(models.Model):
    word_set = models.ForeignKey(Set, on_delete=models.CASCADE)
    word = models.CharField(max_length=128)#單字的英文
    chinese = models.CharField(max_length=128)#單字的中文
    completed = models.ForeignKey(User, on_delete=models.CASCADE)  # 一對多，一個使用者能對多個單字打勾表示完成

    def __str__(self):
        return self.word
