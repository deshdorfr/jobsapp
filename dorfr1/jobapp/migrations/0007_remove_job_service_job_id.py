# Generated by Django 2.2.7 on 2020-07-12 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0006_auto_20200712_0645'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_service',
            name='job_id',
        ),
    ]
