import django_filters

from products.models import Product, Store


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(
        field_name='price', lookup_expr='gte')
    category_name = django_filters.CharFilter(
        field_name='category__name', lookup_expr='icontains')
    adult = django_filters.BooleanFilter(field_name='is_18_plus')

    class Meta:
        model = Product
        fields = {
            # contains, i - case insensitive
            'title': ['icontains'],
            # less than, greater than
            'price': ['lt', 'gt'],
            'category': ['exact'],
            'tags': ['exact'],
            'created_at': ['date__gt', 'date__lt'],
        }

class StoreFilter(django_filters.FilterSet):
    min_employees = django_filters.NumberFilter(field_name='employees_num', lookup_expr='gte')
    max_square = django_filters.CharFilter(field_name='square', lookup_expr='gte')

    class Meta:
        model = Store
        fields = {
            # contains, i - case insensitive
            'name': ['icontains'],
            # less than, greater than
            'square': ['lt', 'gt'],
            'employees_num': ['lt', 'gt'],
        }
