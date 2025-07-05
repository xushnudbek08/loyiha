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



class biz(models.Model):
    text = models.TextField(max_length=500, blank=True, null=True)
  

    def __str__(self):
        return self.text[:50]  # Birinchi 50 belgini qaytaradi
    
class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    text = models.TextField(verbose_name="Izoh matni")
    image = models.ImageField(upload_to='comment_images/', blank=True, null=True, verbose_name="Rasm")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product.name} - {self.user.username} izohi"



