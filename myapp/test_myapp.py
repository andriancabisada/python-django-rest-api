from django.test import TestCase
from myapp.models import Product, Category
from rest_framework.test import APIClient
from rest_framework import status


# class CategoryTestCase(TestCase):
#     def setUp(self):
#         self.category = Category.objects.create(name="Electronics")

#     def test_category_name(self):
#         self.assertEqual(self.category.name, "Electronics")


# class ProductTestCase(TestCase):
#     def setUp(self):
#         # Create a category
#         self.category = Category.objects.create(name="Electronics")

#         # Create a product associated with the category
#         self.product = Product.objects.create(
#             name="Smartphone",
#             description="A modern smartphone",
#             category=self.category,
#         )

#     def test_product_name(self):
#         self.assertEqual(self.product.name, "Smartphone")

#     def test_product_description(self):
#         self.assertEqual(self.product.description, "A modern smartphone")

#     def test_product_category(self):
#         self.assertEqual(self.product.category, self.category)

#     def test_product_category_name(self):
#         # Test accessing the category name through the product
#         self.assertEqual(self.product.category.name, "Electronics")


class CrudTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.category_data = {'name': 'Test Category'}
        self.product_data = {
            'name': 'Test Product',
            'description': 'Test Description',
            # You can set this to a valid category ID if needed.
            'category': None
        }

    def test_create_category(self):
        response = self.client.post('/category/create/', self.category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_create_product(self):
        # Assuming you have created a Category instance here if needed.
        category = Category.objects.create(name='Test Category')
        self.product_data['category'] = category.id

        response = self.client.post('/product/create/', self.product_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)

    def test_read_categories(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_products(self):
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_category(self):
        category = Category.objects.create(name='Test Category')
        updated_data = {'name': 'Updated Category Name'}

        response = self.client.put(
            f'/category/{category.id}/update/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        category.refresh_from_db()
        self.assertEqual(category.name, updated_data['name'])

    def test_update_product(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(
            name='Test Product', category=category)
        updated_data = {'name': 'Updated Product Name'}

        response = self.client.put(
            f'/product/{product.id}/update/', updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        product.refresh_from_db()
        self.assertEqual(product.name, updated_data['name'])

    def test_delete_category(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.delete(f'/category/{category.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)

    def test_delete_product(self):
        category = Category.objects.create(name='Test Category')
        product = Product.objects.create(
            name='Test Product', category=category)
        response = self.client.delete(f'/product/{product.id}/delete/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)
