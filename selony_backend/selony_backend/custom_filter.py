import django_filters

from user_management.models import Address


class AddressFilter(django_filters.FilterSet):

    class Meta:
        model = Address
        fields = ('created_by', 'updated_by')
