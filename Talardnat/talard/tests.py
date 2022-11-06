from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import shop_detail, product, review
from seller.models import seller_detail
from PIL import Image
import tempfile

# Create your tests here.

def create_image(temp_img):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_img, 'png')
    return temp_img

class TalardViewsTest(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='monday', password='monday22', email='monday@morning.com')

        seller1 = seller_detail.objects.create(
            sname = user2
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
            expire = 14,
            queue = 1
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

    def test_index_view(self):
        c = Client()
        response=c.get(reverse('index'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/index.html')

    def test_category_view(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        customer1 = Profile.objects.first()
        response=c.get(reverse('talard',args=[customer1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/category.html')

    def test_allshop_view(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        customer1 = Profile.objects.first()
               
        response=c.get(reverse('allshop', args=[shop1.category, customer1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/allshop.html')

    def test_thisshop_view(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        customer1 = Profile.objects.first()

        response=c.get(reverse('thisshop', args=[customer1.id,shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/shop.html')

    def test_about_view(self):
        c = Client()
        response=c.get(reverse('about'))
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'talard/about.html')

    # def test_buy_view(self):
    #     c = Client()
    #     c.post(reverse('customer_login'),
    #            {'username': 'sunday', 
    #            'password': 'sunday11'})
    #     shop1 = shop_detail.objects.first()
    #     customer1 = Profile.objects.first()
    #     product1 = product.objects.first()

    #     response=c.get(reverse('buy', args=[customer1.id,shop1.id,product1.id]))
    #     # Check response
    #     self.assertTemplateUsed(response, 'talard/shop.html')