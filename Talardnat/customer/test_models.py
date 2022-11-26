from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer import forms
from customer.models import Profile

class CustomerModelsTestCase(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(
            username='sunday', 
            password='sunday11', 
            email='sunday@morning.com',
            first_name='sunday',
            last_name='weekends',
        )

        customer1 = Profile.objects.create(
            customer = user1
        )

    def test_customer(self):
        """test string method of Profile"""
        customer1 = Profile.objects.first()
        self.assertEqual(customer1.__str__(),customer1.customer.username)

    def test_customer_profile(self):
        """test if profile exist"""
        customer1 = Profile.objects.first()
        user1 = User.objects.first()

        self.assertEqual(Profile.objects.count(), 1)
        self.assertEqual(str(customer1.customer), user1.username)
