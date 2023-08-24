from django.test import TestCase
from myapp.models import Product, Category

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Electronics")

    def test_category_name(self):
        self.assertEqual(self.category.name, "Electronics")

class ProductTestCase(TestCase):
    def setUp(self):
        # Create a category
        self.category = Category.objects.create(name="Electronics")

        # Create a product associated with the category
        self.product = Product.objects.create(
            name="Smartphone",
            description="A modern smartphone",
            category=self.category,
        )

    def test_product_name(self):
        self.assertEqual(self.product.name, "Smartphone")

    def test_product_description(self):
        self.assertEqual(self.product.description, "A modern smartphone")

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)

    def test_product_category_name(self):
        # Test accessing the category name through the product
        self.assertEqual(self.product.category.name, "Electronics")
