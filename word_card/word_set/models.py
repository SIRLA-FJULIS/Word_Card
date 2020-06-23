from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Set(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    set_name = models.CharField(max_length=128, unique=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.set_name



class Word(models.Model):
    word = models.CharField(max_length=128)
    chinese = models.CharField(max_length=128)
    completed = False

    def __str__(self):
        return self.word
