# Generated by Django 3.0.7 on 2020-06-29 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_set', '0006_word_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
