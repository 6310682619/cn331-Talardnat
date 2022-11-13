from django.contrib import admin
from .models import shop_detail, product, MyOrder, round
# Register your models here.

class round_fil(admin.ModelAdmin):
    filter_horizontal = ["shop"]

admin.site.register(round, round_fil)
admin.site.register(shop_detail)
admin.site.register(product)
admin.site.register(MyOrder)


