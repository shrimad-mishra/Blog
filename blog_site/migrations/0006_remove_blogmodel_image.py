# Generated by Django 3.2.7 on 2021-09-08 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0005_auto_20210908_1221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel',
            name='image',
        ),
    ]
