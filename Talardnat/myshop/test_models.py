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

        review1 = Review.objects.create(
            user = customer1,
            shop = shop1,
            review_text = "so good",
            review_rating = 5
        )

        order1 = MyOrder.objects.create(
            customer = customer1,
            shop = shop1,
            prod = product1,
            count = 1
        )


    def test_shop_detail(self):
        shop1 = shop_detail.objects.first()
        seller1 = seller_detail.objects.first()

        self.assertEqual(str(shop1.name),'ChocolateFactory')
        self.assertEqual(str(shop1.seller_id), str(seller1.sname))

    def test_product(self):
        product1 = product.objects.first()

        self.assertEqual(str(product1.product_name),'Chocolate bar')
        self.assertEqual(product1.prodprice(), product1.price)
        self.assertTrue(int(product1.id) < 10)
        

    def test_product_ordered(self):
        shop1 = shop_detail.objects.first()
        product1 = product.objects.get(shop=shop1)
        #self.assertEqual(product1.ordered(), product1.count -1)

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

    def test_myorder(self):
        order1 = MyOrder.objects.first()
        self.assertEqual(order1.price(), order1.prod.price * order1.count)

    def test_round(self):
        shop1 = shop_detail.objects.first()
        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
            expire = datetime.datetime.today() + datetime.timedelta(days=10),
            start = datetime.datetime.today()
        )
        round1.shop.set([shop1])
        self.assertEqual(round1.shop.count(), 1)

        self.assertEqual(round1.__str__(),f"round: {round1.round_queue}")