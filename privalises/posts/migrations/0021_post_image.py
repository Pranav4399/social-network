# Generated by Django 3.2.4 on 2021-07-01 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_profile_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_image'),
        ),
    ]
