

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_item', '0002_barangpetani_delete_item'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BarangWishlist',
        ),
    ]
