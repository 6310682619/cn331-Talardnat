from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import shop_detail, product
from seller.models import seller_detail
from talard.models import *
from .models import *
from .forms import *
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
            payment = "1234567"
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

    def test_myshop_index(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        seller1 = seller_detail.objects.first()
        shop1 = shop_detail.objects.first()
        response=c.get(reverse('myshop_index', args=[seller1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/myshop_index.html')
        
        response=c.post(reverse('myshop_index', args=[seller1.id]),{
            'name': shop1.name,
            'category': shop1.category, 
            'in_interact': shop1.in_interact, 
            'ex_interact': shop1.ex_interact, 
            'payment': shop1.payment,
        })
        self.assertEqual(response.status_code, 200)

    def test_myshop_shop(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
        )
        round1.shop.set([shop1])
        queue = (shop1.addqueue.get()).round_queue
        c.post(reverse('myshop', args=[shop1.id]),{'queue':queue})
        response=c.get(reverse('myshop', args=[shop1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/shop.html')

    def test_myshop_queue(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        found = round.objects.all().exists()
        self.assertFalse(found)
        response=c.get(reverse('queue', args=[shop1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/queue.html')

    def test_myshop_delshop(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('delshop', args=[shop1.id]))
        self.assertEqual(response.status_code, 302)

    def test_myshop_product(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('product', args=[shop1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/product.html')
    
    def test_myshop_delproduct(self):
        """test delete product"""
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        product1 = product.objects.first()
        response=c.get(reverse('delprod', args=[shop1.id, product1.id]))
        self.assertEqual(response.status_code, 302)

    def test_myshop_edit(self):
        """test edit myshop"""
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('edit', args=[shop1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/edit.html')

        response=c.post(reverse('edit', args=[shop1.id]),{
            'name': 'NewName',
            'category': shop1.category, 
            'in_interact': shop1.in_interact, 
            'ex_interact': shop1.ex_interact, 
            'payment': shop1.payment,
        })
        self.assertEqual(response.status_code, 302)

    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def test_image_upload(self):
        """test upload product image"""
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        temp_img = tempfile.NamedTemporaryFile()
        test_image = create_image(temp_img)
        image = product.objects.create(product_im=test_image.name)
        response=c.post(reverse('product', args=[shop1.id]),{'product':image})
        self.assertEqual(response.status_code, 200)
        
    def test_myshop_myreview(self):
        """test myreview"""
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        response=c.get(reverse('myreview', args=[shop1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/myreview.html')

    def test_myshop_edit_prod(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        product1 = product.objects.first()
        response=c.get(reverse('editprod', args=[shop1.id, product1.id]))
        self.assertEqual(response.status_code, 200)
        self.failUnless(isinstance(response.context['form'],ProductForm))
        self.assertTemplateUsed(response, 'myshop/editprod.html')
        response=c.post(reverse('editprod', args=[shop1.id, product1.id]),{
            'product_name': 'new chocolate',
            'price': product1.price, 
            'count': product1.count, 
        })
        self.assertEqual(response.status_code, 302)

    def test_myshop_addqueue(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        seller1 = seller_detail.objects.first()
        shop1 = shop_detail.objects.first()
        shop2 = shop_detail.objects.create(
            seller_id = seller1,
            name = "PetShop",
            category = "utensil",
            in_interact = "For your puppy",
            ex_interact = "Puppy care",
        )
        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
            expire = datetime.datetime(2022, 11, 20),
            start = datetime.datetime(2022, 11, 25)
        )
        round1.shop.set([shop1])
        c.post(reverse('addqueue', args=[shop2.id, round1.id]),{
            'shop': shop2,
            'round_queue': round1.round_queue,
            'numshop': (round1.numshop + 1),
            'expire': datetime.datetime(2022, 11, 20),
            'start': datetime.datetime(2022, 11, 25)
        })
        response=c.get(reverse('queue', args=[shop2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myshop/queue.html')

    def test_del_queue(self):
        """test delete queue"""
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        shop1 = shop_detail.objects.first()
        round1 = round.objects.create(
            round_queue = 1,
            numshop = 1,
        )
        round1.shop.set([shop1])
        queue = round.objects.filter(shop=shop1)
        find = queue.exists()
        self.assertTrue(find)
        
        c.get(reverse('delqueue', args=[shop1.id]), follow=True)
        response = c.post(reverse('delqueue', args=[shop1.id]),follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse('queue', args=[shop1.id]), status_code=302)
        
        response = c.delete(reverse('delqueue', args=[shop1.id]))
        self.assertEqual(response.status_code, 302)

    def test_shop_form(self):
        c = Client()
        shop1 = shop_detail.objects.first()
        data={
            'name': 'pudding',
            'category': 'food',
            'in_interact': 'eat it',
            'ex_interact': 'eat',
            'payment': '123',
        }
        c.post(reverse('myshop', args=[shop1.id]), data)
        response = c.get(reverse('myshop', args=(shop1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_new_product(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})
        temp_img = tempfile.NamedTemporaryFile()
        test_image = create_image(temp_img)
        shop1 = shop_detail.objects.first()
        response=c.get(reverse('product', args=[shop1.id]))
        # response = c.post(reverse('product', args=[shop1.id]),{
        #     'product_name': 'popcorn',
        #     'price': 10,
        #     'product_im': test_image,
        #     'count': 20,
        # })
        self.assertEqual(response.status_code, 200)
        product2 = product.objects.create(
            shop = shop1,
            product_name = "Popcorn",
            price = 20,
            product_im=test_image.name,
            count = 10
        )
        prod = product.objects.filter(shop=shop1)
        self.assertEqual(prod.count(),2)