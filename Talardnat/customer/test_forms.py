from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.forms import RegisterForm
from customer.models import Profile

# Create your tests here.

class CustomerFormTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            username='sunday', 
            password='sunday11', 
            email='sunday@morning.com',
            first_name='sunday',
            last_name='weekends',
        )


    # def test_valid_register_form(self):
    #     user1 = User.objects.first()
    #     customer1 = Profile.objects.create(
    #         customer = user1,
    #         address = "Citypark",
    #         city = "TU",
    #         state = "Bkk",
    #         zip = 11111,
    #         phone = "123456789"
    #     )
    #     data={
    #         'username': customer1.customer.username,
    #         'first_name': customer1.customer.first_name,
    #         'last_name': customer1.customer.last_name,
    #         'email': customer1.customer.email,
    #         'password1': customer1.customer.password,
    #         'password2': customer1.customer.password,
    #         'address': customer1.address,
    #         'city': customer1.city,
    #         'state': customer1.state,
    #         'zip': customer1.zip,
    #         'phone': customer1.phone,
    #     }
    #     response = self.client.post(reverse('profile', args=[customer1.id]), data=data)
    #     self.assertEqual(response.status_code, 302)

    def test_invalid_register_form(self):
        user2 = User.objects.create_user(username='monday', password='', email='')
        customer1 = Profile.objects.create(
            customer = user2,
            address = "Citypark",
            city = "TU",
            state = "Bkk",
            zip = 11111,
            phone = "123456789"
        )
        data={
            'username': customer1.customer.username,
            'first_name': customer1.customer.first_name,
            'last_name': customer1.customer.last_name,
            'email': customer1.customer.email,
            'password1': customer1.customer.password,
            'password2': customer1.customer.password,
            'address': customer1.address,
            'city': customer1.city,
            'state': customer1.state,
            'zip': customer1.zip,
            'phone': customer1.phone
        }
        form = RegisterForm(data=data)
        self.assertFalse(form.is_valid())