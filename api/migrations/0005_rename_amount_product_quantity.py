# Generated by Django 4.1 on 2022-08-17 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='amount',
            new_name='quantity',
        ),
    ]