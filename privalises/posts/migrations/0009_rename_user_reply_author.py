# Generated by Django 3.2.4 on 2021-06-15 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210615_1255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reply',
            old_name='user',
            new_name='author',
        ),
    ]
