from django.db import models
import uuid

class Product(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name= models.CharField(max_length=255)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.CharField(max_length=100, blank=True, null=True)
    product_description = models.TextField(blank=True, null=True)
    
