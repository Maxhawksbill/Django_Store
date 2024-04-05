from django.core.management import BaseCommand
from django.db.models import Count

from products.models import Product


class Command(BaseCommand):
    help = 'Test queryset'

    def handle(self, *args, **options):
        # SELECT * FROM products_product
        all_products = Product.objects.all()
        print(all_products)

        # SELECT * FROM products_product WHERE category_id=1
        products = Product.objects.filter(category_id=1)
        print(products)

        # SELECT * FROM products_product WHERE category_id=1 AND price>100
        products = Product.objects.filter(category_id=1, price__gt=100)
        print(products)

        # SELECT * FROM products_product WHERE category_id=1 OR price>100
        # Using OR operator
        products = Product.objects.filter(
            category_id=1) | Product.objects.filter(
            price__gt=100)

        print(products)

        # Exclude
        # SELECT * FROM products_product WHERE NOT (category_id=1 AND
        # price>100)
        products = Product.objects.exclude(category_id=1, price__gt=100)
        print(products)

        # products is a queryset
        # products can be turned into python list
        products_list = list(products)

        # Queryset is lazy
        # lets say here is is 1M products
        long_query = Product.objects.all()

        # long_query is a queryset
        long_query_to_list = list(long_query)

        # shorten the queryset
        # SELECT * FROM products_product where price < 10
        short_query = long_query.filter(price__lt=10)

        # short_query is a queryset
        short_query_to_list = list(short_query)

        # GET - return single object
        # SELECT * FROM products_product WHERE id=1
        product = Product.objects.get(id=1)

        # exceptions, when object does not exist or multiple objects returned
        # DoesNotExist
        # MultipleObjectsReturned

        # Sort by price
        # SELECT * FROM products_product ORDER BY price
        products = Product.objects.order_by('price')

        # Sort by price in descending order
        # SELECT * FROM products_product ORDER BY price DESC
        products = Product.objects.order_by('-price')

        # SELECT * FROM products_product WHERE price>100 ORDER BY price DESC
        products = Product.objects.filter(price__gt=100).order_by('-price')

        # Sort by multiple fields
        # SELECT * FROM products_product ORDER BY price DESC, title
        products = Product.objects.order_by('-price', 'title')

        # Group by category
        # SELECT category_id, COUNT(*) FROM products_product GROUP BY
        # category_id
        products = Product.objects.values(
            'category_id').annotate(count=Count('id'))

        # Group by category, show average price
        # SELECT category_id, AVG(price) FROM products_product GROUP BY
        # category_id
        average_price_py_category = Product.objects.values(
            'category_id').annotate(avg_price=Count('price'))

        # For every product set price which is average for the category
        for product in all_products:
            product.price = average_price_py_category.get(
                category_id=product.category_id)['avg_price']
            product.save()

        # Create new product
        # INSERT INTO products_product (title, price, category_id) VALUES ('New
        # product', 100, 1)
        new_product = Product.objects.create(
            title='New product', price=100, category_id=1)

        # Update
        # UPDATE products_product SET price=200 WHERE id=1
        product = Product.objects.get(id=1)
        product.price = 200
        product.save()

        # Delete
        # DELETE FROM products_product WHERE id=1
        product = Product.objects.get(id=1)
        product.delete()
