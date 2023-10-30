import graphene

from graphene_django import DjangoObjectType

from product_management.models import (Category, Attribute, AttributeChoice,
                                       ProductClass, Product, ProductVariant,
                                       ProductImage, ProductStock)

from user_management.schema.types.address import AddressType


class CategoryType(DjangoObjectType):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'slug')
        interfaces = (graphene.relay.Node, )


class CategoryConnection(graphene.relay.Connection):

    class Meta:
        node = CategoryType


class AttributeChoiceType(DjangoObjectType):

    class Meta:
        model = AttributeChoice
        fields = ('id', 'value', 'attribute')
        interfaces = (graphene.relay.Node, )


class AttributeChoiceConnection(graphene.relay.Connection):

    class Meta:
        node = AttributeChoiceType


class AttributeType(DjangoObjectType):

    class Meta:
        model = Attribute
        fields = ('name', 'description', 'attributechoice_set')
        interfaces = (graphene.relay.Node, )

    attributechoice_set = graphene.relay.ConnectionField(AttributeChoiceConnection)

    def resolve_attributechoice_set(parent, info, **kwargs):
        return parent.attributechoice_set.all()


class AttributeTypeConnection(graphene.relay.Connection):

    class Meta:
        node = AttributeType


class ProductClassType(DjangoObjectType):

    class Meta:
        model = ProductClass
        fields = ('id', 'name', 'description',
                  'has_variant', 'attributes')
        interfaces = (graphene.relay.Node, )


class ProductClassConnection(graphene.relay.Connection):

    class Meta:
        node = ProductClassType


class ProductImageType(DjangoObjectType):

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product', 'variant')
        interfaces = (graphene.relay.Node, )


class ProductImageConnection(graphene.relay.Connection):

    class Meta:
        node = ProductImageType


class ProductStockType(DjangoObjectType):

    class Meta:
        model = ProductStock
        fields = ('id', 'quantity', 'actual_price', 'location',
                  'variant')
        interfaces = (graphene.relay.Node, )


class ProductStockConnection(graphene.relay.Connection):

    class Meta:
        node = ProductStockType


class ProductType(DjangoObjectType):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price',
                  'category', 'product_class', 'attibutes',
                  'productimage_set')
        interfaces = (graphene.relay.Node, )

    product_class = graphene.Field(ProductClassType)
    productimage_set = graphene.relay.ConnectionField(ProductImageConnection)

    def resolve_productimage_set(root, info, **kwargs):
        return root.productimage_set.all()


class ProductConnection(graphene.relay.Connection):

    class Meta:
        node = ProductType


class ProductVariantType(DjangoObjectType):

    class Meta:
        model = ProductVariant
        fields = ('id', 'name', 'description', 'price',
                  'product', 'attibutes', 'productimage_set',
                  'productstock_set')
        interfaces = (graphene.relay.Node, )

    product = graphene.Field(ProductType)
    productimage_set = graphene.relay.ConnectionField(ProductImageConnection)
    productstock_set = graphene.relay.ConnectionField(ProductStockConnection)

    def resolve_productimage_set(root, info, **kwargs):
        return root.productimage_set.all()

    def resolve_productstock_set(root, info, **kwargs):
        return root.productstock_set.all()


class ProductVariantConnection(graphene.relay.Connection):

    class Meta:
        node = ProductVariantType
