# Generated by Django 3.0.7 on 2020-06-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_set', '0005_remove_word_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='completed',
            field=models.BooleanField(default=True),
        ),
    ]
