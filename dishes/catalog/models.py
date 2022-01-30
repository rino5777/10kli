from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='category/',)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'קטרגוריות'
        ordering =('name',)

    def get_absolute_url(self):
        return reverse('catalog:Subcategory', args = [self.slug ] )


    def __str__(self):
        return str(self.name)




class Subcategory(models.Model):
    name = models.CharField(max_length=100, unique =True)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subcategory/',)
    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Subcategory'
        verbose_name_plural = 'תת קטגוריות'
        ordering =('name',)

    def get_absolute_url(self):

        return reverse('catalog:product_detail', args=[self.category.slug, self.slug])

class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique = True, primary_key=True, editable=False, max_length=30, blank=True)
    name = models.CharField(max_length=100, db_index=True)
    slug  = models.SlugField(max_length=100, db_index=True)

    image = models.ImageField( upload_to='photo/%Y/%m/%d', null=True, blank=True )
    
    chort_word = models.CharField("краткое описание ", max_length = 150)
    word = models.TextField("полное описание")
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    adv = models.CharField("תיאור לקידום", max_length = 500, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return str(self.name)

        
    class Meta:
        ordering =('name', ) 
        index_together =(('id','slug'), )

    def get_absolute_url(self):

        return reverse('catalog:product', args=[self.id, self.slug]) 