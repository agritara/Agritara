# Generated by Django 4.1 on 2022-10-30 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemda_home', '0002_remove_orderhistory_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='review',
            field=models.TextField(default=''),
        ),
    ]
