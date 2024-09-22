from django.db import models

# Create your models here.

from Optician.utils.base import BaseModel

class Blog(BaseModel):

    title = models.CharField(max_length=100, verbose_name='Title of the blog cart', help_text='max 100 characters')
    # datetime = models.DateTimeField(verbose_name='datetime of tche blog cart')
    image = models.ImageField(verbose_name='Image of the blog cart')
    description = models.TextField(verbose_name='Text of the blog cart')
    # is_published = models.BooleanField(default=False, verbose_name='Is published?')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"
            

class Comments(BaseModel):

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment_of_th_blog')
    name = models.CharField(max_length=100,verbose_name='Comment name')
    email = models.EmailField(verbose_name='Comment email')
    comment = models.TextField(verbose_name='Comment')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "All comments"

