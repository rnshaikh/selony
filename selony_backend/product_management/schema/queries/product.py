import graphene

from django.db.models import Avg, Count 

from graphene_django.filter import DjangoFilterConnectionField

from django.shortcuts import get_object_or_404

from product_management.models import (Category, ProductClass,
                                       Product, ProductVariant,
                                       ProductImage, ProductStock,
                                       ProductReview)
from product_management.schema.types.product import (ProductType,
                                                     ProductVariantType,
                                                     CategoryConnection,
                                                     ProductClassConnection,
                                                     ProductImageType,
                                                     ProductStockType,
                                                     ProductReviewType,
                                                     ProductReviewImageType)

from selony_backend.custom_decorator import permission_required
from selony_backend.custom_permission import is_authenticated
from selony_backend.custom_filter import (ProductFilter, VariantFilter,
                                          ProductImageFilter, ProductStockFilter,
                                          ProductReviewFilter)


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

    product = graphene.relay.Node.Field(ProductType)
    products = DjangoFilterConnectionField(ProductType,
                                           filterset_class=ProductFilter)

    product_variant = graphene.relay.Node.Field(ProductVariantType)
    product_variants = DjangoFilterConnectionField(ProductVariantType,
                                                   filterset_class=VariantFilter)
    product_images = DjangoFilterConnectionField(ProductImageType,
                                                 filterset_class=ProductImageFilter)
    product_stocks = DjangoFilterConnectionField(ProductStockType,
                                                 filterset_class=ProductStockFilter)

    product_review = graphene.relay.Node.Field(ProductReviewType)
    product_reviews = DjangoFilterConnectionField(ProductReviewType,
                                                  filterset_class=ProductReviewFilter)


    @permission_required(is_authenticated)
    def resolve_product(root, info, id):
        product_obj = get_object_or_404(Product, id=id)
        return product_obj

    @permission_required(is_authenticated)
    def resolve_products(root, info, **kwargs):
        return Product.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_variant(root, info, id):
        product_variant_obj = get_object_or_404(ProductVariant, id=id)
        return product_variant_obj

    @permission_required(is_authenticated)
    def resolve_product_variants(root, info, **kwargs):
        variants = ProductVariant.objects.all().annotate(total_reviews=Count('productreview__id'),
                                                         avg_rating=Avg('productreview__rating'))
        return variants

    @permission_required(is_authenticated)
    def resolve_product_images(root, info, **kwargs):
        return ProductImage.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_stocks(root, info, **kwargs):
        return ProductStock.objects.all()

    @permission_required(is_authenticated)
    def resolve_product_review(root, info, id):
        rev_obj = get_object_or_404(ProductReview, id=id)
        return rev_obj

    @permission_required(is_authenticated)
    def resolve_product_reviews(root, info, **kwargs):
        return ProductReview.objects.all()
