from django.test import TestCase

from category.models import ProductCategory, BlogCategory


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = ProductCategory.objects.create(
            name='test_name',
            slug='test_name',
            description='test_description'
        )
        self.data2 = BlogCategory.objects.create(
            name='test_name',
            slug='test_name',
            description='test_description'
        )

    def test_product_category_model_entry(self):
        """
        Test product category model data insertion/type/fields attributes
        """
        data = self.data1

        self.assertTrue(isinstance(data, ProductCategory))
        self.assertEqual(str(data), 'test_name')

    def test_blog_category_model_entry(self):
        """
        Test blog category model data insertion/type/fields attributes
        """
        data = self.data2

        self.assertTrue(isinstance(data, BlogCategory))
        self.assertEqual(str(data), 'test_name')
