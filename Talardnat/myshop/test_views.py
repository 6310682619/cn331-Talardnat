from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import shop_detail, product
from seller.models import seller_detail
from talard.models import *
from myshop import forms
from .models import *
from PIL import Image
import tempfile
from django.test import override_settings
import datetime

# Create your tests here.
      
def create_image(temp_img):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_img, 'png')
    return temp_img


class MyShopViewsTest(TestCase):
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
            name = "ChocolatePudding",
            category = "food",
            in_interact = "Chocolate Pudding Yummy",
            ex_interact = "Come and get it!",
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

        # round0 = round.objects.create(
        #     shop = shop1,
        #     round_queue = 0,
        #     numshop = 1,
        #     expire = datetime.datetime.today() + datetime.timedelta(days=10),
        #     start = datetime.datetime.today()
        # )


    def test_myshop_index(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        seller1 = seller_detail.objects.first()
        response=c.get(reverse('myshop_index', args=[seller1.id]))

        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'myshop/myshop_index.html')
        self.failUnless(isinstance(response.context['form'],
                                   forms.ShopForm))

    def test_myshop_shop(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        response=c.get(reverse('myshop', args=[shop1.id]))
        
        # Check response
        self.assertEqual(response.status_code, 200)
        # Check template
        self.assertTemplateUsed(response, 'myshop/shop.html')

    def test_myshop_delshop(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('delshop', args=[shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 302)

    def test_myshop_product(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('product', args=[shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        self.failUnless(isinstance(response.context['form'],
                                   forms.ProductForm))
        # Check template
        self.assertTemplateUsed(response, 'myshop/product.html')
    
    def test_myshop_delproduct(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        product1 = product.objects.first()
        response=c.get(reverse('delprod', args=[shop1.id, product1.id]))
        # Check response
        self.assertEqual(response.status_code, 302)

    def test_myshop_edit(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('edit', args=[shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        self.failUnless(isinstance(response.context['form'],
                                   forms.ShopForm))
        # Check template
        self.assertTemplateUsed(response, 'myshop/edit.html')

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
            pic = product.objects.first()
            self.assertEqual(len(product.objects.all()), 1)
        
    def test_myshop_review(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        review1 = Review.objects.first()
        
        response=c.get(reverse('myreview', args=[shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Review.objects.count(), 1)
        # Check template
        self.assertTemplateUsed(response, 'myshop/myreview.html')

    def test_myshop_edit_prod(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        product1 = product.objects.first()
        response=c.get(reverse('editprod', args=[shop1.id, product1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        self.failUnless(isinstance(response.context['form'],
                                   forms.ProductForm))
        # Check template
        self.assertTemplateUsed(response, 'myshop/editprod.html')

    def test_del_shop(self):
        c = Client()
        c.post(reverse('customer_login'),
               {'username': 'monday', 
               'password': 'monday22'})

        shop1 = shop_detail.objects.all()
        shop1.delete()
        self.assertEqual(shop1.count(), 0)

    def test_shop_form(self):
        shop1 = shop_detail.objects.first()
        data={
            'name': 'pudding',
            'category': 'food',
            'in_interact': 'eat it',
            'ex_interact': 'eat',
            'payment': '123',
        }
        response = self.client.post(reverse('myshop', args=(shop1.id,)), data=data)
        self.assertEqual(response.status_code, 200)

    def test_product_form(self):
        temp_img = tempfile.NamedTemporaryFile()
        test_image = create_image(temp_img)
        shop1 = shop_detail.objects.first()
        data={
            'product_name': 'pudding',
            'price': 10,
            'count': 'eat it',
            'product_im': test_image.name,
        }
        response = self.client.post(reverse('product', args=(shop1.id,)), data=data)
        self.assertEqual(response.status_code, 200)