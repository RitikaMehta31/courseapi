# Generated by Django 3.2.3 on 2021-07-09 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hom', '0004_auto_20210708_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='user',
        ),
    ]
