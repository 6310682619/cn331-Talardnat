from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.forms import RegisterForm

# Create your tests here.

# class CustomerFormTest(TestCase):
#     def test_registerform(self):
#         form = RegisterForm()
#         assert False is form.is_valid()