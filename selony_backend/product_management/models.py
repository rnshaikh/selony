from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from user_management.models import Address

from selony_backend.model_mixin import CreateUserInfo, UpdateUserInfo


def directory_path(instance, filename):

    return 'product_{0}/{1}/{2}'.format(instance.product.category.name,
                                        instance.product.name,filename)


class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class AttributeChoice(models.Model):

    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value


class ProductClass(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    has_variant = models.BooleanField(default=False)
    attributes = models.ManyToManyField(Attribute, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_class = models.ForeignKey(ProductClass, on_delete=models.CASCADE)
    attibutes = models.ManyToManyField(Attribute)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attibutes = models.ManyToManyField(AttributeChoice)

    def __str__(self):
        return self.name


class ProductImage(models.Model):

    image = models.FileField(upload_to=directory_path)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variant = models.ForeignKey(ProductVariant, blank=True,
                                null=True, on_delete=models.CASCADE)

    def __str__(self):

        if self.variant:
            return self.variant.name
        return self.product.name


class ProductStock(models.Model):

    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    location = models.ForeignKey(Address, on_delete=models.CASCADE)
    actual_price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.variant.name


class ProductReview(CreateUserInfo, UpdateUserInfo):

    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1),
                                             MaxValueValidator(5)])
    review = models.CharField(max_length=512, blank=True, null=True)
