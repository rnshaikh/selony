from django.db import models

from user_management.models import Address


def directory_path(instance, filename):

    return 'product_{0}/{1}/{2}'.format(instance.product.category.name,
                                        instance.product.name,filename)


class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.TextField(blank=True, null=True)


class Attribute(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()


class AttributeChoice(models.Model):

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)


class ProductClass(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    has_variant = models.BooleanField(default=False)
    attributes = models.ManyToManyField(Attribute,
                                        on_delete=models.CASCADE)


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    attibutes = models.ManyToManyField(Attribute)


class ProductVariant(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=10)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attibutes = models.ManyToManyField(Attribute)


class ProductImage(models.Model):

    image = models.FileField(upload_to=directory_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)


class ProductStock(models.Model):

    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=10)
