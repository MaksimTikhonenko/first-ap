from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField(null=False, default=0)
    expire_date = models.DateTimeField(null=True)
    product_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.product_id}/{self.name}/{self.category}"
