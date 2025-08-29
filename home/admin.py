from django.contrib import admin
from home.models import Product,Profile

class Admin_Product(admin.ModelAdmin):
    list_display=('product_id','product_name','product_price','product_stock','product_image','product_seller_id','product_category','product_description','product_created_at','product_updated_at')
admin.site.register(Product, Admin_Product)

class Admin_Profile(admin.ModelAdmin):
    list_display=('user','phone_number','profile_image')
admin.site.register(Profile,Admin_Profile)
