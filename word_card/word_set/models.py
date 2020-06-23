from django.db import models

# Create your models here.
class Set(models.Model):
    name = models.CharField(max_length=128, unique=True)
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pubDateTime']  # 發表單字集的時間順序反向顯示


class Word(models.Model):
    word = models.CharField(max_length=128)
    chinese = models.CharField(max_length=128)
    completed = False

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['-pubDateTime']
