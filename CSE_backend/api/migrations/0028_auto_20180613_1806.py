# Generated by Django 2.0.5 on 2018-06-13 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_auto_20180611_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default='anonymous', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to=settings.AUTH_USER_MODEL),
        ),
    ]
