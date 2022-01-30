from django.db import models
from django.urls import reverse
# Create your models here.
class Content(models.Model):

    
    slug  = models.SlugField('слаг', max_length=100, db_index=True)
    image_1 = models.ImageField("1 картинка ( на главной и на главной блога )", upload_to='blog/%Y/%m/%d', null=True, blank=True )
    image_2 = models.ImageField(" 2 картинка, ( не обязательно )", upload_to='blog/%Y/%m/%d', null=True, blank=True )  
    chort_entry = models.TextField("краткое описание ", max_length = 150)
    name_entry_1 = models.CharField('название текста 1',max_length=400, db_index=True, null=True, blank=True)
    #big_word = models.CharField('большая буква которая относится к первому тексту', max_length=1, null=True, blank=True )
    entry_1 = models.TextField("полное описание 1",  null=True, blank=True)
    entry_in_block = models.TextField("текст в блоке",  null=True, blank=True)
    name_entry_2 = models.CharField('название текста 2',max_length=400, db_index=True, null=True, blank=True)
    entry_2 = models.TextField("полное описание 2", null=True, blank=True)
    datetime = models.DateTimeField(null=True, blank=True)
    autor = models.CharField(max_length = 50, null=True, blank=True)
    keywords = models.CharField('for seo',max_length = 1000, null=True, blank=True)
    


    def __str__(self):
        return str(self.name_entry_1 or self.name_entry_2 )

    def get_absolute_url(self):
        return reverse('blog:content', args=[self.slug])