# Generated by Django 4.2.5 on 2023-10-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='attibutes',
            field=models.ManyToManyField(to='product_management.attributechoice'),
        ),
    ]
