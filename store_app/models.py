from django.db import models

# Create your models here.  

class ProductManager(models.Manager):
    def prod_validator(self, postData):
        errors = {}
        if len(postData['name'])<8:
            errors['name'] = "Product Name should be at least 8 characters long."
        if len(postData['price'])<1:
            errors['price-len'] = "Must have a price."
        if float(postData['price'])<0.01:
            errors['price'] = "Price must be greater than $ 0.00."
        if len(postData['description'])>50:
            errors['description'] = "Description must be less than 50 characters."
        if len(postData['description'])<8:
            errors['description'] = "Description must be at least 8 characters."
        return errors
    
class MfgManager(models.Manager):
    def mfg_validator(self, postData):
        errors = {}
        if len(postData['name'])<2:
            errors['name'] = "Manufacturer name should be at least 2 characters long."
        return errors
    
class Manufacturers(models.Model):
    name = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    objects = MfgManager()
    def __str__(self):
        return self.name
        
    

class Products(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.FloatField(blank=False)
    description = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    manufacturer = models.ForeignKey(Manufacturers, related_name='products', on_delete=models.CASCADE, blank=False)
    objects = ProductManager()