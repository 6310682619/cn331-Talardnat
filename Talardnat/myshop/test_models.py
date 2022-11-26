from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import *
from seller.models import seller_detail
from myshop import forms
from talard.models import *
import datetime

# Create your tests here.

class MyShopModelsTest(TestCase):
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
            name = "ChocolateFactory",
            category = "food",
            in_interact = "Chocoland Wonderland",
            ex_interact = "A land of Chocolate",
        )

        # shop2 = shop_detail.objects.create(
        #     seller_id = seller1,
        #     name = "PetShop",
        #     category = "utensil",
        #     in_interact = "For your puppy",
        #     ex_interact = "Puppy care",
        # )

        product1 = product.objects.create(
            shop = shop1,
            product_name = "Chocolate bar",
            price = 50,
            count = 1
        )

        customer1 = Profile.objects.create(
            customer = user2,
            address = "Citypark",
            city = "TU",
            state = "Bkk",
            zip = 11111,
            phone = "123456789"
        )

        order1 = MyOrder.objects.create(
            customer = customer1,
            shop = shop1,
            prod = product1,
            count = 1
        )


    def test_shop_detail(self):
        """test string method of model shop_detail"""
        shop1 = shop_detail.objects.first()
        seller1 = seller_detail.objects.first()

        self.assertEqual(shop1.name.__str__(),'ChocolateFactory')
        self.assertEqual(shop1.seller_id.__str__(), seller1.sname.__str__())

    def test_product(self):
        """test method of model product"""
        product1 = product.objects.first()

        self.assertEqual(product1.product_name.__str__(),'Chocolate bar')
        self.assertEqual(product1.prodprice(), product1.price)

    def test_product_available(self):
        """test if product available"""
        product1 = product.objects.first()
        c = product1.prodcount()
        self.assertTrue(c > 0)

    def test_product_not_available(self):
        """test if product not available"""
        product1 = product.objects.first()
        c = product1.prodcount()
        c-=1
        self.assertFalse(c > 0)

    def test_myorder(self):
        """test method of model MyOrder"""
        order1 = MyOrder.objects.first()
        self.assertEqual(order1.price(), order1.prod.price * order1.count)

    def test_round(self):
        """test string method of model round"""
        shop1 = shop_detail.objects.first()
        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
        )
        round1.shop.set([shop1])
        self.assertEqual(round1.shop.count(), 1)
        self.assertEqual(round1.__str__(),f"round: {round1.round_queue}")