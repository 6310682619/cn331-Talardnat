from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.forms import RegisterForm
from customer.models import Profile
from seller.models import seller_detail
from django.http import HttpRequest
from . import views

# Create your tests here.

class CustomerViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='monday', password='monday11', email='monday@morning.com')

        customer1 = Profile.objects.create(
            customer = user1,
            address = "Citypark",
            city = "TU",
            state = "Bkk",
            zip = 11111,
            phone = "123456789"
        )

        seller1 = seller_detail(sname=user2)

    def test_profile(self):
        """Test if user can access profile"""
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        customer1 = Profile.objects.first()
        response = c.get(reverse('profile', args=[customer1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'customer/profile.html')

    def test_not_profile(self):
        """Test if user not customer"""
        c = Client()
        c.login(username='monday', password='monday11')
        seller1 = User.objects.get(username='monday')
        response = c.get(reverse('profile', args=[seller1.id]))
        self.assertEqual(response.status_code, 302)

    def test_login_view(self):
        """Test if user can login"""
        c = Client()
        response = c.get(reverse('customer_login'))
        # Check response
        self.assertEqual(response.status_code, 200)

    def test_logged_out(self):
        """Test if user can logout"""
        c = Client()
        response = c.get(reverse('customer_logout'))

        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['message'] == 'You are logged out!')
        # Check template
        self.assertTemplateUsed(response, 'customer/login.html')

    def test_not_user_login(self):
        """Test if user put wrong password"""
        c = Client()
        response = c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'tuesday3'})
        
        self.assertTrue(response.context['message'] == 'Invalid credentials.')

        response = c.get(reverse('customer_login'))
        self.assertEqual(response.status_code, 200)

        response = c.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_register_get(self):
        """Test uncorrect register data"""
        c = Client()
        response = c.get(reverse('register'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'customer/register.html')

        self.failUnless(isinstance(response.context['form'],
                                   RegisterForm))

    def test_register_post(self):
        """Test correct register data"""
        c = Client()
        form_data = {
            'username': "demo",
            'first_name': "demo",
            'last_name': "demo",
            'email': "demo@example.com",
            'password1': "demopassword",
            'password2': "demopassword",
            'address': "demoA",
            'city': "demoC",
            'state': "demoS",
            'zip': 12345,
            'phone': 12345
        }
        c.post(reverse('register'),form_data)
        response = c.get(reverse("customer_login"))
        self.assertEqual(response.status_code, 200)