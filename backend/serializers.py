from .models import MenuCategory, MenuItem, Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'price_retail', 'price_wholesale', 'stock_quantity', 'sku', 'created_at', 'updated_at']
        
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id', 'name', 'description']


class MenuItemSerializer(serializers.ModelSerializer):
   
    category = MenuCategorySerializer(read_only=True)
  
    category_id = serializers.PrimaryKeyRelatedField(queryset=MenuCategory.objects.all(), source='category', write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'image', 'category', 'category_id', 'is_available']