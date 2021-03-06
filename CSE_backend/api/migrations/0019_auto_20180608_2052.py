# Generated by Django 2.0.5 on 2018-06-08 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='category',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='roomkey',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='value',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
