from django.db import models

# Create your models here.

from user.models import CustomUser
from product.models import ProductVersion

class WishList(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE, related_name='user_wishlist')
    product = models.ManyToManyField(ProductVersion, related_name='product_wishlist')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s wishlist"
    
    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishLists'

class BasketItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_basket')
    product = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name='product_basket')
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s basket"
    
    def get_subtotal(self):
        return self.product.product.price * self.quantity
    
    class Meta:
        verbose_name = 'BasketItem'
        verbose_name_plural = 'BasketItems'

class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_basket_item')
    items = models.ManyToManyField(BasketItem, related_name='basket_item')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s basket"
    
    class Meta:
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'