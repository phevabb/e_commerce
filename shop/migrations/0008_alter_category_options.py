# Generated by Django 4.2.4 on 2023-10-11 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_price_currency_alter_product_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]