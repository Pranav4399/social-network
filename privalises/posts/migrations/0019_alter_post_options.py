# Generated by Django 3.2.4 on 2021-06-29 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20210629_1951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_posted', '-shared_on']},
        ),
    ]
