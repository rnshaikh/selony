import graphene

from product_management.models import (Category, ProductClass,
                                       Product, ProductVariant,
                                       ProductImage, ProductStock)
from product_management.schema.types.product import (CategoryConnection,
                                                     ProductClassConnection,
                                                     ProductConnection,
                                                     ProductVariantConnection,
                                                     ProductImageConnection,
                                                     ProductStockConnection)

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated


class CategoryQueries(graphene.ObjectType):

    categories = graphene.relay.ConnectionField(CategoryConnection)


    @permission_required(is_authenticated)
    def resolve_categories(root, info, **kwargs):
        return Category.objects.all()


class ProductClassQueries(graphene.ObjectType):

    product_classes = graphene.relay.ConnectionField(ProductClassConnection)

    @permission_required(is_authenticated)
    def resolve_product_classes(root, info, **kwargs):
        return ProductClass.objects.all()


class ProductQueries(graphene.ObjectType):

    products = graphene.relay.ConnectionField(ProductConnection)
    product_variants = graphene.relay.ConnectionField(ProductVariantConnection)
    product_images = graphene.relay.ConnectionField(ProductImageConnection)
    product_stocks = graphene.relay.ConnectionField(ProductStockConnection)

    @permission_required(is_authenticated)
    def resolve_products(root, info, **kwargs):
        return Product.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_variants(root, info, **kwargs):
        return ProductVariant.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_images(root, info, **kwargs):
        return ProductImage.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_stocks(root, info, **kwargs):
        return ProductStock.objects.all()
