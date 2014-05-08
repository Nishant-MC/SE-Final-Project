from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('Other', 'Other'),
    ('BOOKS','Books'),
    ('CLOTHES','Clothes'),
    ('COOKING','Cooking'),
    ('COSMETICS','Cosmetics'),
    ('ELECTRONICS','Electronics'),
    ('FOOD','Food'),
    ('INSTRUMENTS','Instruments'),   
    ('STATIONERY','Stationery'),
    ('TOOLS','Tools'),  
)


class Item(models.Model):
    #code
    item_name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=25, choices = CATEGORY_CHOICES, default='Other')
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    checked_out_date = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=False )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    owner = models.ForeignKey(User)
    
    def __unicode__(self):
        return smart_unicode(self.item_name)
