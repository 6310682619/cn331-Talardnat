from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from customer.models import Profile
from myshop.models import shop_detail, product, review
from seller.models import seller_detail
from myshop import forms
from PIL import Image
import tempfile
from django.test import override_settings

# Create your tests here.
      
def create_image(temp_img):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new("RGBA", size, color)
    image.save(temp_img, 'png')
    return temp_img


class MyShopViewsTest(TestCase):
    def setUp(self):

        user1 = User.objects.create_user(username='sunday', password='sunday11', email='sunday@morning.com')
        user2 = User.objects.create_user(username='monday', password='monday22', email='monday@morning.com')

        seller1 = seller_detail.objects.create(
            sname = user1
        )

        shop1 = shop_detail.objects.create(
            seller_id = seller1,
            name = "ChocolatePudding",
            category = "food",
            in_interact = "Chocolate Pudding Yummy",
            ex_interact = "Come and get it!",
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

        customer1 = Profile.objects.create(
            customer = user2
        )

        review1 = review.objects.create(
            customer = customer1,
            shop = shop1,
            score = 10,
            description = "I love Chocolate so much."
        )

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
            # temp_img = tempfile.NamedTemporaryFile()
            # test_image = create_image(temp_img)

            pic = product.objects.first()
            self.assertEqual(len(product.objects.all()), 1)
        
    def test_myshop_review(self):
        c = Client()
        c.post(reverse('seller_login'),
               {'username': 'sunday', 
               'password': 'sunday11'})

        shop1 = shop_detail.objects.first()
        review1 = review.objects.first()
        
        response=c.get(reverse('myreview', args=[shop1.id]))
        # Check response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(review.objects.count(), 1)
        # Check template
        self.assertTemplateUsed(response, 'myshop/myreview.html')