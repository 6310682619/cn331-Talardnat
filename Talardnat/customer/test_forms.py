from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.forms import RegisterForm
from customer.models import Profile
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomerFormTest(TestCase):
    def setUp(self)-> None:
        self.username = 'sunday'
        self.first_name = 'sunday'
        self.last_name = 'morning'
        self.email = 'sunday@morning.com'
        self.password1 = 'Cn331Tu'
        self.password2 = 'Tu331Cn'

    def test_register_form(self):
        c = Client()
        response = c.post(reverse('register'), data={
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'password1': self.password1,
            'password2': self.password2
        })
        self.assertEqual(response.status_code, 200)