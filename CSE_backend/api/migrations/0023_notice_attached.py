# Generated by Django 2.0.5 on 2018-06-09 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20180610_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='attached',
            field=models.ManyToManyField(blank=True, related_name='notice', to='api.Attached'),
        ),
    ]
