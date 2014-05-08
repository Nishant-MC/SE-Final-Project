from django import forms
from .models import Item

class AddInventoryForm(forms.ModelForm):
    
    class Meta:
        model = Item
        categor = forms.ChoiceField(choices = ['Food', 'Things', 'Information'])
        fields = ('item_name', 'description', 'category')
        
    def save(self, username, commit=True):
        item = super(AddInventoryForm,self).save(commit=False)
        item.available = True
        item.owner = username
        item.owner = category
        item.checked_out_date = None
        if commit:
            item.save()
        return item
    
    
    
    
    #item_name = models.CharField(max_length=120, null=True, blank=True)
    #description = models.TextField(max_length=300, null=True, blank=True)
    #category = models.CharField(max_length=25, null=True, blank = True)
    
    
    #added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    #checked_out_date = models.DateTimeField( blank=True)
    #available = models.BooleanField(default=False )
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)
   # owner = models.ForeignKey(User)