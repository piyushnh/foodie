# Generated by Django 2.0.1 on 2018-01-31 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0004_auto_20180131_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normaluser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='userprofiles/profile_pics'),
        ),
    ]
