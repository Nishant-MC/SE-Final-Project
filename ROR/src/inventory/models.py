from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Item(models.Model):
    #code
    item_name = models.CharField(max_length=120, null=True, blank=True)
    description = models.TextField(max_length=300, null=True, blank=True)
    category = models.CharField(max_length=25, null=True, blank = True)
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    checked_out_date = models.DateTimeField( blank=True)
    available = models.BooleanField(default=False )
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    
    def __unicode__(self):
        return smart_unicode(self.item_name)
