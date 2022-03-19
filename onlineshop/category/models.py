from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='product_category/images/', null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Product Categories'

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_category/images/', null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name
