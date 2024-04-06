from django.test import TestCase, Client
from django.urls import reverse
from .models import EarlyInterest

class EarlyRegisterViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('early_register')

    def test_get_early_register(self):
        """Test GET request to EarlyRegister view"""
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 200, 'message': 'Register for early interest in ScalerFest 2024'})

    def test_post_early_register_duplicate_email(self):
        """Test POST request to EarlyRegister view with duplicate email"""
        EarlyInterest.objects.create(email='test@example.com', phone='1234567890')
        data = {'email': 'test@example.com'}
        response = self.client.post(self.register_url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'status': 200, 'message': 'User registered successfully'})
        self.assertEqual(EarlyInterest.objects.filter(email='test@example.com').count(), 1)

class EarlyInterestModelTestCase(TestCase):
    def test_email_field(self):
        """Test email field of EarlyInterest model"""
        email = EarlyInterest.objects.create(email='test@example.com', phone='1234567890')
        self.assertEqual(str(email), 'test@example.com')

    def test_unique_email_constraint(self):
        """Test unique email constraint of EarlyInterest model"""
        EarlyInterest.objects.create(email='test@example.com', phone='1234567890')
        with self.assertRaises(Exception):
            EarlyInterest.objects.create(email='test@example.com', phone='0987654321')