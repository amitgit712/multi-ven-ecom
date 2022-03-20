from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from category.models import ProductCategory
from products.models import Product


class TestViewResponse(TestCase):

    def setUp(self):
        self.client = Client()
        category = ProductCategory.objects.create(
            name='prod_category',
            slug='prod_category',
            description='description',
            image='category.img'
        )
        user = get_user_model().objects.create_user(
            email='test@user.com', password='pass'
        )

        self.data1 = Product.objects.create(
            category_id=category.id,
            created_by_id=user.id,
            name='product_name',
            description='product_description',
            image='product.img',
            slug='product_name',
            price='20.00'
        )

    def test_product_detail_url(self):
        '''
        Test product respnse detail status
        '''
        response = self.client.get(reverse(
            'products:product_detail', args=[self.data1.slug]
        ))
        self.assertEqual(response.status_code, 200)
