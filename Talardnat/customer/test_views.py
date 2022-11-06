from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer import forms
from customer.models import Profile

# Create your tests here.

class CustomerViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user1.save()

    def test_profile(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        response = c.get(reverse('profile'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'customer/profile.html')

    def test_login_view(self):
        c = Client()
        response = c.get(reverse('customer_login'))
        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_out(self):
        c = Client()
        response = c.get(reverse('customer_logout'))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['message'] == 'You have been logged out!')
        # Check template
        self.assertTemplateUsed(response, 'customer/login.html')

    def test_not_user_login(self):
        c = Client()
        response = c.post(reverse('customer_login'),
               {'username': 'user3', 
               'password': 'tuesday3'})
        # Check response
        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('customer_login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_register_get(self):
        c = Client()
        response = c.get(reverse('register'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'customer/register.html')

        self.failUnless(isinstance(response.context['form'],
                                   forms.RegisterForm))

    def test_register_success(self):
        c = Client()
        response = c.post(reverse('register'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        response = c.get(reverse('profile'))
        # Check response
        self.assertEqual(response.status_code, 302)