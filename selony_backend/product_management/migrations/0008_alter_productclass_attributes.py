# Generated by Django 4.2.5 on 2023-12-10 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0007_alter_productclass_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productclass',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='product_management.attribute'),
        ),
    ]
