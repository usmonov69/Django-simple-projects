# Generated by Django 3.2.7 on 2021-09-30 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_barcode_product_barcodee'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='country_id',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer_id',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=-6, max_length=5),
            preserve_default=False,
        ),
    ]