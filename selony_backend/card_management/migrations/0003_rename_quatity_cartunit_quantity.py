# Generated by Django 4.2.5 on 2023-11-11 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_management', '0002_rename_card_cart_rename_cardunit_cartunit_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartunit',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
