# Generated by Django 2.0.1 on 2018-03-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_auto_20180330_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='website_url',
            field=models.URLField(default='', max_length=100),
        ),
    ]
