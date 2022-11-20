from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from myshop.models import *
from .models import *
from . import forms
from django.http import HttpRequest
from . import views

# Create your tests here.

class SellerViewsTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username='sunday', 
            password='sunday11', 
            email='sunday@morning.com',
            first_name='sunday',
            last_name='weekends',
        )
        
        user2 = User.objects.create_user(
            username='monday', 
            password='monday22', 
            email='monday@morning.com',
            first_name='monday',
            last_name='weekdays',
        )

        seller1 = seller_detail.objects.create(
            sname = user1
        )

        shop1 = shop_detail.objects.create(
            seller_id = seller1,
            name = "DarkChocolate",
            category = "food",
            in_interact = "Dark Chocolate is sweet",
            ex_interact = "Buy it or Buy it!",
            payment = "12312121"
        )

    def test_index(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        seller1 = seller_detail.objects.first()
        response = c.get(reverse('seller_index', args=[seller1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'seller/seller_index.html')

    def test_login_view(self):
        c = Client()
        response = c.get(reverse('seller_login'))
        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_out(self):
        c = Client()
        response = c.get(reverse('seller_logout'))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['message'] == 'You are logged out')
        # Check template
        self.assertTemplateUsed(response, 'seller/seller_login.html')

    def test_not_user_login(self):
        c = Client()
        response = c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'tuesday3'})
        # Check response
        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('seller_login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('taview'))
        self.assertEqual(response.status_code, 200)

    def test_not_seller(self):
        """Test if user not customer"""
        c = Client()
        c.login(username='monday', password='monday22')
        customer1 = User.objects.get(username='monday')
        response = c.get(reverse('seller_index', args=[customer1.id]))
        self.assertEqual(response.status_code, 302)

    def test_signup_get(self):
        c = Client()
        response = c.get(reverse('seller_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/seller_signup.html')

    def test_signup_post(self):
        """Test correct signup"""
        c = Client()
        form_data={
            'username':'sunday',  
            'email':'sunday@morning.com',
            'first_name':'sunday',
            'last_name':'weekends',
            'password1': 'sunday11',
            'password2': 'sunday11'
        }
        
        c.post(reverse('seller_signup'), form_data)
        response = c.get(reverse('seller_login'))
        self.assertEqual(response.status_code, 200)