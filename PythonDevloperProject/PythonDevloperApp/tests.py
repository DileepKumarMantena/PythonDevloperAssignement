from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.parsers import MultiPartParser
from .models import BooksModel  
from .serializers import BookPostSerializer

class BooksPostApiTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_books_post_api_success(self):
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
        }
        response = self.client.post('http://127.0.0.1:8000/DjangoApp /BokksPostApi/', data, format='multipart')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['message'], 'Successful')
        self.assertFalse(response.data['HasError'])
        self.assertTrue('Result' in response.data)
        serialized_data = BookPostSerializer(BooksModel.objects.get(pk=response.data['Result']['id'])).data
        self.assertEqual(response.data['Result'], serialized_data)

    def test_books_post_api_fail(self):
        data = {
        }
        response = self.client.post('http://127.0.0.1:8000/DjangoApp /BokksPostApi/', data, format='multipart')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['message'], 'Fail')      

class GetBooksAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_books_success(self):
        data=[BooksModel.objects.create(title="Book 1", author="Author 1"),
        BooksModel.objects.create(title="Book 2", author="Author 2")]

        response = self.client.post('http://127.0.0.1:8000/DjangoApp /GetBooks/', data, format='multipart')

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data['Message'], 'Successful')
        self.assertFalse(response.data['HasError'])
        self.assertEqual(len(response.data['Result']), 2)  
        
    def test_get_books_failure(self):
        data=[]
        response = self.client.post('http://127.0.0.1:8000/DjangoApp /GetBooks/', data, format='multipart')

        self.assertEqual(response.status_code, 400)

        self.assertEqual(response.data['Message'], 'Fail')
        self.assertTrue(response.data['HasError'])
        self.assertEqual(len(response.data['Result']), 0)
