# Generated by Django 3.0.7 on 2020-06-29 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('word_set', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='published_date',
        ),
        migrations.AddField(
            model_name='word',
            name='completed',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='word_set',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='word_set.Set'),
            preserve_default=False,
        ),
    ]
