from django.contrib import admin
from .models import shop_detail, product, review, MyOrder
# Register your models here.
admin.site.register(shop_detail)
admin.site.register(product)
admin.site.register(review)
admin.site.register(MyOrder)