# Generated by Django 4.2.5 on 2023-10-29 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0002_alter_productvariant_attibutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product_management.productvariant'),
        ),
    ]