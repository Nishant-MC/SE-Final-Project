from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Notification
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.context_processors import csrf
from inventory.models import Item
from datetime import datetime
# Create your views here.

def show_notification(request, notification_id):
    
    n = Notification.objects.get(id=notification_id)
    args = {}
    args['notification'] = n
    args['user'] = request.user
    return render_to_response('notification.html', args)



def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('/')


def request_page(request, item_id=''):
    
    args = {}
    args.update(csrf(request))
    #title = 'Request from %s'%str(request.user)
    item = Item.objects.get(id = item_id)
    #Notification.objects.create(user=name, title=title, message=message, sender=request.user)
    args['borrower'] = request.user
    args['item'] = item
    
    return render_to_response('requestform.html',args)

def request_item(request, lender='', item_id=''):
    
    if request.method == 'POST':
        title=request.POST.get('title','')
        message = request.POST.get('message','')
        urgent = request.POST.get('urgent','')
        receiver = User.objects.get(username=lender)
        sender = request.user
        m_type = 'request'
        item = Item.objects.get(id=item_id)
        Notification.objects.create(item = item, receiver=receiver, title=title, message=message, sender=request.user, urgent = urgent, m_type = m_type)
        
    args = {}
    args.update(csrf(request))
    args['name'] = str(receiver)
    args['user_name'] = str(request.user)
    
    return render_to_response('request_success.html',args)
        

    
def accept(request, receiver='', item_id='', notification_id=''):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    
    args = {}
    args.update(csrf(request))
    holder = User.objects.get(username = receiver)
    item_name = Item.objects.get(id=item_id).item_name
    title = '%s has accepted your request for %s'%(str(request.user.first_name),item_name)
    message="You can pick it up soon! :) "
    Notification.objects.create(item = Item.objects.get(id=item_id),receiver=holder, title=title, message=message, sender=request.user, m_type = 'response')
    item = Item.objects.get(id=item_id)
    item.available=False
    item.checked_out_date=datetime.now()
    item.holder=holder
    item.save()
    args['name'] = holder
    args['user_name'] = receiver
    
    return render_to_response('request_success.html',args)
    
    
def deny(request, receiver='', notification_id=''):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = receiver)
    title = 'Deny from %s'%str(request.user)
    message="Sorry! It's not available at the moment!"
    Notification.objects.create(item=None, receiver=name, title=title, message=message, sender=request.user.first_name, m_type = 'response')
    args['name'] = name
    args['user_name'] = receiver
    
    return render_to_response('request_success.html',args)
    
       
    