from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    
class Deal(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='deal_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
