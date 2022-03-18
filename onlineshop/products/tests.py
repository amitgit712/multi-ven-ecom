from django.test import TestCase
from django.contrib.auth import get_user_model

from products.models import Product
from category.models import ProductCategory


class TestProductsModel(TestCase):

    def setUp(self):
        category = ProductCategory.objects.create(
            name='prod_category',
            slug='prod_category',
            description='description'
        )

        user = get_user_model().objects.create_user(
            email='test@user.com', password='pass'
        )

        self.data1 = Product.objects.create(
            category_id=category.id,
            created_by_id=user.id,
            name='product_name',
            description='product_description',
            image='product.png',
            slug='product_name',
            price='20.00'
        )

    def test_product_model_entry(self):
        '''
        Test product model data insertion/types/fields attributes
        '''
        data = self.data1

        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'product_name')
