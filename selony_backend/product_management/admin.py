from django.contrib import admin

from product_management.models import (Category, Attribute, AttributeChoice,
                                       ProductClass, Product, ProductVariant,
                                       ProductImage, ProductStock, ProductReview,
                                       ProductReviewImage)


admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeChoice)
admin.site.register(ProductClass)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)
admin.site.register(ProductStock)
admin.site.register(ProductReview)
admin.site.register(ProductReviewImage)
