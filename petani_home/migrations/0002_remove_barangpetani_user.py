# Generated by Django 4.1 on 2022-11-02 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petani_home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barangpetani',
            name='user',
        ),
    ]
