from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.
from time import time
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

def get_upload_file_name(instance, filename):
    return 'uploaded_files/%s_%s'%(str(time()).replace('.','_'), filename)

class Item(models.Model):
    #code
    item_name = models.CharField(max_length=120, null=False, blank=False)
    description = models.TextField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=25, choices = CATEGORY_CHOICES, default='Other', null=True)
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    checked_out_date = models.DateTimeField(null=True, blank=True)
    available = models.BooleanField(default=True )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    owner = models.ForeignKey(User,related_name = 'owner')
    holder = models.ForeignKey(User, related_name = 'holder', null=True)
    due_date = models.DateTimeField(null=True, blank=True)
    photo = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)
    
    def __unicode__(self):
        return smart_unicode(self.item_name)
