<<<<<<< HEAD
# Generated by Django 4.1 on 2022-10-29 10:59
=======
# Generated by Django 4.1 on 2022-10-30 03:31
>>>>>>> fcc9f8b6eb5b6a287ddd687b3be92e406887e704

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pemda_home', '0002_remove_orderhistory_request_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderhistory',
            name='review',
<<<<<<< HEAD
            field=models.TextField(default='0000000'),
=======
            field=models.TextField(default=''),
>>>>>>> fcc9f8b6eb5b6a287ddd687b3be92e406887e704
        ),
    ]
