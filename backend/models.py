from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)
    category = models.ForeignKey(MenuCategory, related_name='items', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    def __str__(self): 
        return self.name
    
class Item(models.Model):
    ITEM_CATEGORY_CHOICES = (
        ('retail', 'Retail'),
        ('wholesale', 'Wholesale'),
    )

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=ITEM_CATEGORY_CHOICES)
    price_retail = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_wholesale = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock_quantity = models.PositiveIntegerField()
    sku = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
