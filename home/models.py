from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
import uuid

class Profile(models.Model):
       user=models.OneToOneField(User, on_delete=models.CASCADE)
       phone_number=models.CharField(max_length=13, default=None)
       profile_image=models.ImageField(upload_to="profile_images", default=None)
       def __str__(self):
              return self.user.username

class Product(models.Model):
 product_id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
 product_name=models.CharField(max_length=255,default=None)
 product_price=models.DecimalField(max_digits=10, decimal_places=2, default=None)
 product_stock=models.PositiveBigIntegerField(default=1,validators=[MinValueValidator(1)])
 product_image=models.ImageField(upload_to="products_images", default=None)
 product_seller_id=models.ForeignKey(User, on_delete=models.CASCADE, default=User)
 product_category=models.CharField(max_length=255, default=None)
 product_description=models.TextField(default=None)
 product_created_at=models.DateTimeField(auto_now_add=True)
 product_updated_at=models.DateTimeField(auto_now=True)
 def __str__(self):
        return self.product_name
 