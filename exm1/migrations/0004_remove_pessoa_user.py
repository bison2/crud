# Generated by Django 3.1.5 on 2021-01-07 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exm1', '0003_pessoa_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pessoa',
            name='user',
        ),
    ]
