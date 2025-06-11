from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.URLField()
    release_date = models.DateField(verbose_name='Дата события', help_text='Формат: ГГГГ-ММ-ДД') 
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True, db_index=True, )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.id}: {self.name}, цена: {self.price}'
    
