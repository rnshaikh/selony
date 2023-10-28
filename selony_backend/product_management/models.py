from django.db import models


def directory_path(instance, filename):

    return 'product_{0}/{1}/{2}'.format(instance.product.category.name,
                                        instance.product.name,filename)


class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.TextField(blank=True, null=True)


class ProductClass(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    has_variant = models.BooleanField(default=False)


class Attribute(models.Model):
    pass


class AttributeChoice(models.Model):
    pass


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
    pass


