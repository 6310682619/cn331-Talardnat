from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer import forms
from customer.models import Profile

class CustomerModelsTestCase(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')

        customer1 = Profile.objects.create(
            customer = user1
        )

    def test_customer_profile(self):
        customer1 = Profile.objects.first()
        self.assertEqual(Profile.objects.count(), 1)
