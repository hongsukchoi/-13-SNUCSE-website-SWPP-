# Generated by Django 2.0.5 on 2018-06-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20180610_0130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notice',
            name='attached',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='image',
        ),
    ]
