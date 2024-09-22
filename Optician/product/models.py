from django.db import models
from django.urls import reverse
    
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

class Manufacturer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"
    
class Color(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"
    
class Image(models.Model):
    name = models.ImageField(upload_to='product')             

    def __str__(self):
        return f'{self.id}'
    
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

class Product(models.Model):

    name = models.CharField(max_length=100)
    old_price = models.PositiveIntegerField()
    in_sale = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='product_manufacturer')

    @property
    def get_version(self):
        for version in self.versions.all():
            return version.pk

    @property
    def total_quantity(self):
        return sum([version.quantity or 0 for version in self.versions.all()])
    
    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"pk": self.get_version})

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name  
    
class ProductVersion(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='versions'
    )
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='product_version_color')
    cover_image = models.ImageField(upload_to='product')
    image = models.ManyToManyField(Image)
    # quantity = models.IntegerField(verbose_name='Quantity of the product', help_text='Quantity in number', null=True, blank=True)
    # is_main = models.BooleanField(default=False, verbose_name='Is this the main version of product?')

    def __str__(self):
        return f"{self.product.name}'s {self.color.name} version"   

    class Meta:
        verbose_name = 'Product Version'
        verbose_name_plural = 'Product Versions'    

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})