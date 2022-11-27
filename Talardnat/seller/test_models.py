from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from seller.models import seller_detail

# Create your tests here.

class SellerModelsTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='sunday',
         password='sunday11', email='sunday@morning.com')
         
        seller1 = seller_detail.objects.create(sname = user1)

    def test_seller(self):
        """test string method of model seller_detail"""
        seller1 = seller_detail.objects.first()
        self.assertEqual(str(seller1),'sunday')
        self.assertEqual(seller1.__str__(), str(seller1.sname.username))

    def test_seller_detail(self):
        """test if seller is user"""
        seller1 = seller_detail.objects.first()
        user1 = User.objects.first()
        self.assertEqual(str(seller1.sname), user1.username)