from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer import forms
from customer.models import Profile
from django.http import HttpRequest
from . import views

# Create your tests here.

class CustomerViewTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')

        customer1 = Profile.objects.create(
            customer = user1,
            address = "Citypark",
            city = "TU",
            state = "Bkk",
            zip = 11111,
            phone = "123456789"
        )

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
        c = Client()
        response = c.get(reverse('register'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'customer/register.html')

        self.failUnless(isinstance(response.context['form'],
                                   forms.RegisterForm))

    def test_register_post(self):
        customer1 = Profile.objects.first()
        request = HttpRequest()
        request.method = 'POST'
        request.POST['username'] = customer1.customer.username
        request.POST['password'] = customer1.customer.password
        request.POST['first_name'] = customer1.customer.first_name
        request.POST['last_name'] = customer1.customer.last_name
        request.POST['address'] = customer1.address
        request.POST['city'] = customer1.city
        request.POST['state'] = customer1.state
        request.POST['zip'] = customer1.zip
        request.POST['phone'] = customer1.phone
        request.META['HTTP_HOST'] = 'localhost'
        response = views.register(request)
        self.assertEquals(response.status_code, 200)