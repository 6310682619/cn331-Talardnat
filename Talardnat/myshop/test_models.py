from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import *
from seller.models import seller_detail
from myshop import forms
from talard.models import *

# Create your tests here.

class MyShopModelsTest(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='monday', password='monday22', email='monday@morning.com')

        seller1 = seller_detail.objects.create(
            sname = user1
        )

        shop1 = shop_detail.objects.create(
            seller_id = seller1,
            name = "ChocolateFactory",
            category = "food",
            in_interact = "Chocoland Wonderland",
            ex_interact = "A land of Chocolate",
        )

        product1 = product.objects.create(
            shop = shop1,
            product_name = "Chocolate bar",
            price = 50,
            count = 1
        )

        customer1 = Profile.objects.create(
            customer = user2
        )

        review1 = Review.objects.create(
            user = customer1,
            shop = shop1,
            review_text = "so good",
            review_rating = 5
        )


    def test_shop_detail(self):
        shop1 = shop_detail.objects.first()
        seller1 = seller_detail.objects.first()

        self.assertEqual(str(shop1.name),'ChocolateFactory')
        self.assertEqual(str(shop1.seller_id), str(seller1.sname))

    def test_product(self):
        product1 = product.objects.first()

        self.assertEqual(str(product1.product_name),'Chocolate bar')
        self.assertEqual(int(product1.price), 50)
        self.assertEqual(str(product1.price), '50.00')
        self.assertTrue(int(product1.id) < 10)

    def test_review(self):
        review1 = Review.objects.first()
        shop1 = shop_detail.objects.first()

        self.assertEqual(review1.review_rating, 5)
        self.assertEqual(review1.shop, shop1)
        self.assertTrue(len(review1.review_text) < 300)

    def test_product_available(self):
        product1 = product.objects.first()
        c = product1.prodcount()
        self.assertTrue(c > 0)

    def test_product_not_available(self):
        product1 = product.objects.first()
        c = product1.prodcount()
        c-=1
        self.assertFalse(c > 0)