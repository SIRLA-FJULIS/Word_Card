# Generated by Django 3.0.7 on 2020-07-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_set', '0008_auto_20200702_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='chinese',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
