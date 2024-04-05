from django.test import TestCase

from products.models import Product


class IntegrationTestCase(TestCase):
    def test_products_api(self):
        Product.objects.create(
            title='A product',
            price=40,
            summary='A summary')

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.json()['results'], [{'title': 'A product', 'price': 40, 'summary': 'A summary'}])

        self.assertEqual(response.json()['results'][0]['title'], 'A product')
        self.assertEqual(response.json()['results'][0]['price'], 40)
        self.assertEqual(response.json()['results'][0]['summary'], 'A summary')

    def test_products_18_plus(self):
        Product.objects.create(
            title='A product',
            price=40,
            summary='A summary',
            is_18_plus=True)

        response = self.client.get('/api/products/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['results'], [])
