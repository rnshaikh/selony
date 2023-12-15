import django_filters

from graphene_django.filter import (GlobalIDMultipleChoiceFilter,
                                    GlobalIDFilter)


from user_management.models import Address
from product_management.models import (Product,
                                       ProductVariant,
                                       ProductImage,
                                       ProductStock,
                                       ProductReview)


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

    id = GlobalIDFilter(field_name="id")
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

    id = GlobalIDFilter(field_name="id")
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


class ProductImageFilter(django_filters.FilterSet):

    id = GlobalIDFilter(field_name="id")

    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'variant')


class ProductStockFilter(django_filters.FilterSet):

    id = GlobalIDFilter(field_name="id")

    class Meta:
        model = ProductStock
        fields = ('id', 'variant', 'actual_price')


class ProductReviewFilter(django_filters.FilterSet):

    id = GlobalIDFilter(field_name="id")
    from_date = django_filters.DateFilter(method="from_date_filter")
    to_date = django_filters.DateFilter(method="to_date_filter")

    class Meta:
        model = ProductReview
        fields = ('id', 'rating', 'variant', 'from_date',
                  'to_date')

    def from_date_filter(self, qs, name, value):
        return qs.filter(created_at__date__gte=value).distinct()

    def to_date_filter(self, qs, name, value):
        return qs.filter(created_at__date__lte=value).distinct()

