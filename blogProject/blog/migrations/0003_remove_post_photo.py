# Generated by Django 4.0.4 on 2023-05-18 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]