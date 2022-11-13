from django.test import TestCase, Client
from .models import *

class ReviewTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='monday', password='monday22', email='monday@morning.com')

        seller1 = seller_detail.objects.create(
            sname = user1
        )

        customer1 = Profile.objects.create(
            customer = user2
        )

        shop1 = shop_detail.objects.create(
            seller_id = seller1,
            name = "ChocolateLover",
            category = "food",
            in_interact = "Chocolate is the best",
            ex_interact = "Your favourite Choco!",
        )

        review = Review.objects.create(
            user = customer1,
            shop = shop1,
            review_text = "so good",
            review_rating = 5
        )

        rateus1 = RateUs.objects.create(
            user = user2,
            rate_text = "cute",
            rating = 5
        )

    def test_review_model(self):
        r = Review.objects.first()
        self.assertTrue(isinstance(r, Review))
        self.assertEqual(r.__str__(), str(r.review_rating))

    def test_rateus_model(self):
        r = RateUs.objects.first()
        self.assertTrue(isinstance(r, RateUs))
        self.assertEqual(r.__str__(), str(r.rating))