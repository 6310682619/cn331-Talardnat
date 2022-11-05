from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

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

        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('index'))
        self.assertEqual(response.status_code, 302)