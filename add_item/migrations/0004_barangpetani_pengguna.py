# Generated by Django 4.1 on 2022-11-02 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('add_item', '0003_delete_barangwishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='barangpetani',
            name='pengguna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
