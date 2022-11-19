from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from .forms import *
from customer.models import Profile
from myshop.models import *
from seller.models import *
from PIL import Image
import tempfile
import datetime

# Create your tests here.

def create_image(temp_img):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_img, 'png')
    return temp_img

class TalardViewsTest(TestCase):
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

        customer1 = Profile.objects.create(
            customer = user2,
            address = "Citypark",
            city = "TU",
            state = "Bkk",
            zip = 11111,
            phone = "123456789"
        )

        shop1 = shop_detail.objects.create(
            seller_id = seller1,
            name = "ChocolateLover",
            category = "food",
            in_interact = "Chocolate is the best",
            ex_interact = "Your favourite Choco!",
            payment = "12312121"
        )

        temp_img = tempfile.NamedTemporaryFile()
        test_image = create_image(temp_img)

        product1 = product.objects.create(
            shop = shop1,
            product_name = "Chocolate",
            price = 50,
            product_im=test_image.name,
            count = 10
        )

        review1 = Review.objects.create(
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

        order1 = MyOrder.objects.create(
            customer = customer1,
            shop = shop1,
            prod = product1,
            count = 1
        )

        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
            start = datetime.datetime(2022, 11, 17),
            expire = datetime.datetime(2022, 11, 20)
        )
        round1.shop.set([shop1])

    def test_index_view(self):
        """Test if homepage is accessible, check response and template"""
        
        c = Client()
        response=c.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/index.html')

    def test_category_view(self):
        """Test if page is accessible, check response and template"""

        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})
        customer1 = Profile.objects.first()
        response=c.get(reverse('talard',args=[customer1.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/category.html')

    def test_allshop_view(self):
        """Test if page is accessible, check response and template"""

        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})
        shop1 = shop_detail.objects.first()
        customer1 = Profile.objects.first()
               
        response=c.get(reverse('allshop', args=[shop1.category, customer1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/allshop.html')


    def test_about_view(self):
        """Test if about page is accessible, check response and template"""

        c = Client()
        response=c.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/about.html')

    def test_not_user_rateus(self):
        """Test if unauthorized user rate website will return login page"""
        
        c = Client()
        c.post(reverse('rating'),
            {'rate_text' : 'good',
                'rating' : 5})
        response=c.get(reverse('customer_login'))
        self.assertEqual(response.status_code, 200)

    def test_user_rateus(self):
        """Test if authorized user rate website"""
        
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})
        response=c.get(reverse('rating'))
        self.assertEqual(response.status_code, 200)
        response=c.get(reverse('rateus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/rate.html')

    def test_order(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})

        user2 = User.objects.filter(username='monday')
        customer1 = Profile.objects.first()
        myorder = MyOrder.objects.first()
        response=c.post(reverse('order', args=[user2.id]),{
            "order" : myorder, 
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(MyOrder.objects.all().exists())

    def test_del_order(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})

        count = MyOrder.objects.all()
        count.delete()
        self.assertEqual(count.count(), 0)

    def test_valid_rating(self):
        rateus1 = RateUs.objects.first()
        data={
            "user": rateus1.user,
            "rate_text": rateus1.rate_text,
            "rating": rateus1.rating
        }
        response = self.client.post(reverse('rating'), data=data)
        self.assertEqual(response.status_code, 302)

    def test_rateus_view(self):
        """Test if page is accessible, check response and template"""

        c = Client()
        response=c.get(reverse('rateus'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'talard/rate.html')

    def test_thisshop_view(self):
        c = Client()
        user2 = User.objects.get(username='monday')
        shop1 = shop_detail.objects.first()
        round1 = round.objects.first()
        ex = round1.expire
        product1 = product.objects.first()
        reviews = Review.objects.filter(shop=shop1)
        avg_reviews = reviews.aggregate(avg_rating = Avg('review_rating'))

        response=c.post(reverse('thisshop',args=[user2.id, shop1.id]), {
            "this_shop" : shop1,
            "menu" : product1,
            "reviews": reviews,
            "avg_reviews": avg_reviews,
            "expire":ex,
        })
        self.assertEqual(response.status_code, 200)
 
    # def test_addReview(self):
    #     c = Client()
    #     try:
    #         customer1 = Profile.objects.first()
    #     except Profile.DoesNotExist:
    #         pass
    #     shop1 = shop_detail.objects.first()
    #     review1 = Review.objects.first()
    #     response=c.post(reverse('addreview', args=[customer1.id, shop1.id]),{
    #         'review_text': review1.review_text,
    #         'review_rating': review1.review_rating, 
    #     })
    #     self.assertEqual(response.status_code, 302)