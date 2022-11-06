from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import shop_detail, product, review
from seller.models import seller_detail
from myshop import forms

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
            expire = 14,
            queue = 1
        )

        product1 = product.objects.create(
            shop = shop1,
            product_name = "Chocolate bar",
            price = 50,
            count = 10
        )

        customer1 = Profile.objects.create(
            customer = user2
        )

        review1 = review.objects.create(
            customer = customer1,
            shop = shop1,
            score = 10,
            description = "Bitter but Sweet"
        )

    def test_shop_detail(self):
        shop1 = shop_detail.objects.first()
        seller1 = seller_detail.objects.first()

        self.assertEqual(str(shop1.name),'ChocolateFactory')
        self.assertEqual(str(shop1.seller_id), str(seller1.sname))
        self.assertEqual(shop1.queue, 1)

    def test_product(self):
        product1 = product.objects.first()

        self.assertEqual(str(product1.product_name),'Chocolate bar')

    def test_review(self):
        review1 = review.objects.first()
        shop1 = shop_detail.objects.first()

        self.assertEqual(review1.score, 10)
        self.assertEqual(review1.shop, shop1)