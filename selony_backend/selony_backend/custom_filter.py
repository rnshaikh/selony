import django_filters

from graphene_django.filter import GlobalIDMultipleChoiceFilter


from user_management.models import Address
from product_management.models import (Product,
                                       ProductVariant)


class NumberInFilter(django_filters.BaseInFilter,
                     django_filters.NumberFilter):
    pass


class CharInFilter(django_filters.BaseInFilter,
                   django_filters.CharFilter):
    pass


class AddressFilter(django_filters.FilterSet):

    class Meta:
        model = Address
        fields = ('created_by', 'updated_by')


class ProductFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name='price',
                                            lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='lte')
    product_class = GlobalIDMultipleChoiceFilter(field_name='product_class')
    category = GlobalIDMultipleChoiceFilter(field_name="category")

    class Meta:
        model = Product
        fields = ('id', 'category', 'product_class',
                  'min_price', 'max_price')


class VariantFilter(django_filters.FilterSet):

    min_price = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price',
                                            lookup_expr='lte')
    product_class = GlobalIDMultipleChoiceFilter(field_name='product__product_class')
    category = GlobalIDMultipleChoiceFilter(field_name="product__category")

    class Meta:
        model = ProductVariant
        fields = ('id', 'category', 'product',
                  'product_class', 'category',
                  'min_price', 'max_price')
