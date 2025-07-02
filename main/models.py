from django.db import models
from django.contrib.auth.models import User






class Category(models.Model):    
    name = models.CharField(max_length=100)

  
    def __str__(self):
        return self.name



class color(models.Model):
    name = models.CharField(max_length=100)



    def __str__(self):
        return self.name    
    

class ssd(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey('color', on_delete=models.CASCADE, null=True, blank=True)
    ssd = models.ForeignKey('ssd', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
    



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # boshqa maydonlar
    def __str__(self):
        return self.user.username
