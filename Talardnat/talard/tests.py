from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class TalardViewTest(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user1.save()

    def test_index_view(self):
        c = Client()
        response=c.get(reverse('index'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/index.html')