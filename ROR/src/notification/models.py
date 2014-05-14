from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import Item
# Create your models here.

class Notification(models.Model):
    item = models.ForeignKey(Item, related_name = 'item', null=True)
    title = models.CharField(max_length=256)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    receiver = models.ForeignKey(User, related_name = 'receiver')
    sender = models.ForeignKey(User, related_name = 'sender')
    send_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    urgent = models.BooleanField(default=False)
    m_type = models.CharField(max_length=256,  null=True, blank=True)
    


'''    
@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
    if kwargs.get('created',False):
        Notification.objects.create(user=kwargs.get('instance'),
                                    title="Welcome to Room of Requirement page!",
                                    message="Thank you for joining us!")
'''