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
        fields = ('id', 'value')
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


class ProductType(DjangoObjectType):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price',
                  'category', 'product_class', 'attibutes')
        interfaces = (graphene.relay.Node, )

    product_class = graphene.Field(ProductClassType)


class ProductConnection(graphene.relay.Connection):

    class Meta:
        node = ProductType


class ProductVariantType(DjangoObjectType):

    class Meta:
        model = ProductVariant
        fields = ('id', 'name', 'description', 'price',
                  'product', 'attibutes')
        interfaces = (graphene.relay.Node, )

    product = graphene.Field(ProductType)


class ProductVariantConnection(graphene.relay.Connection):

    class Meta:
        node = ProductVariant


class ProductImageType(DjangoObjectType):

    class Meta:
        model = ProductImage
        fields = ('id', 'image', 'product', 'variant')
        interfaces = (graphene.relay.Node, )

    product = graphene.Field(ProductType)
    variant = graphene.Field(ProductVariantType)


class ProductImageConnection(graphene.relay.Connection):

    class Meta:
        node = ProductImageType


class ProductStockType(DjangoObjectType):

    class Meta:
        model = ProductStock
        fields = ('id', 'quantity', 'actual_price', 'location',
                  'variant')
        interfaces = (graphene.relay.Node, )

    location = graphene.Field(AddressType)
    variant = graphene.Field(ProductVariantType)


class ProductStockConnection(graphene.relay.Connection):

    class Meta:
        node = ProductStockType

