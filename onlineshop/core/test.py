from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase

from category.models import ProductCategory
from core.views import homepage
from products.models import Product


class TestViewResponse(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        category = ProductCategory.objects.create(
            name='prod_category',
            slug='prod_category',
            description='description',
            image='category.img'
        )
        user = get_user_model().objects.create_user(
            email='test@user.com', password='pass'
        )

        Product.objects.create(
            category_id=category.id,
            created_by_id=user.id,
            name='product_name',
            description='product_description',
            image='product.img',
            slug='product_name',
            price='20.00'
        )

    def test_url_allowed_host(self):
        '''
        Test allowed host
        '''
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = homepage(request)
        html = response.content.decode('utf-8')
        self.assertIn('<home></home>', html)
        self.assertTrue(html.startswith('\n<!doctype html>\n'))
        self.assertEqual(response.status_code, 200)

    def test_view_function(self):
        request = self.factory.get('/product/product_name/')
        response = homepage(request)
        html = response.content.decode('utf-8')
        self.assertIn('<home></home>', html)
        self.assertTrue(html.startswith('\n<!doctype html>\n'))
        self.assertEqual(response.status_code, 200)
