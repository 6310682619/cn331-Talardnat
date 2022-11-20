from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from myshop.models import *
from seller.models import seller_detail
from seller import forms

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

    def test_signup_get(self):
        c = Client()
        response = c.get(reverse('seller_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'seller/seller_signup.html')

    def test_signup_post(self):
        c = Client()
        response = c.post(reverse('seller_signup'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        seller1 = seller_detail.objects.first()

        response = c.post(reverse('seller_index', args=[seller1.id]),{
            'username':'sunday', 
            'password':'sunday11', 
            'email':'sunday@morning.com',
            'first_name':'sunday',
            'last_name':'weekends'
        })
        self.assertEqual(response.status_code, 302)