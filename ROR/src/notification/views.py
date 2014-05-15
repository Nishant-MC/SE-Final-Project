from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Notification
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.context_processors import csrf
from inventory.models import Item
from datetime import datetime
from datetime import timedelta
from userprofile.models import UserProfile
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
        duration = request.POST.get('duration','')
        item = Item.objects.get(id=item_id)
        if urgent:
            expiry_day = datetime.now() + timedelta(minutes=1)
        else:
            expiry_day = datetime.now() + timedelta(days=30)
        Notification.objects.create(item = item, receiver=receiver, title=title, message=message, sender=request.user, urgent = urgent, m_type = m_type, duration=duration, status='Pending', expiry_day = expiry_day)
        
    args = {}
    args.update(csrf(request))
    args['name'] = receiver.first_name
    args['item'] = item.item_name
    
    return render_to_response('request_success.html',args)
        

    
def accept(request, receiver='', item_id='', notification_id=''):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.status = 'Accepted'
    days = int(n.duration)
    n.save()
    lender = UserProfile.objects.get(user=request.user)
    lender.lend_credit+=1
    lender.save()
    args = {}
    args.update(csrf(request))
    holder = User.objects.get(username = receiver)
    item_name = Item.objects.get(id=item_id).item_name
    title = '%s has accepted your request for %s'%(str(request.user.first_name),item_name)
    message="You can pick it up soon! :) "
    expiry_day = datetime.now() + timedelta(days=30)
    Notification.objects.create(item = Item.objects.get(id=item_id),receiver=holder, title=title, message=message, sender=request.user, m_type = 'response', expiry_day=expiry_day)
    item = Item.objects.get(id=item_id)
    item.available=False
    item.checked_out_date=datetime.now()
    item.due_date = datetime.now() + timedelta(days=days)
    item.holder=holder
    item.save()
    args['name'] = holder.first_name
    args['status'] = 'accepted'
    
    return render_to_response('response.html',args)
    
    
def deny(request, receiver='', notification_id=''):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.status = 'Denied'
    n.save()
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = receiver)
    title = 'Deny from %s'%str(request.user.first_name)
    message="Sorry! It's not available at the moment!"
    expiry_day = datetime.now() + timedelta(days=30)
    Notification.objects.create(item=None, receiver=name, title=title, message=message, sender=request.user, m_type = 'response', expiry_day=expiry_day)
    args['name'] = name.first_name
    args['status'] = 'denied'
    return render_to_response('response.html',args)
    
def inbox(request, option='in'):
    if option=='' or option=='in':
        m = Notification.objects.filter(receiver=request.user)
    else:
        m = Notification.objects.filter(sender=request.user)
    args = {}
    args.update(csrf(request))
    args['messages'] = m
    args['type'] = option
    return render_to_response('inbox.html',args)
    
    
def rate(request, user_name='', notification_id=''):
    args = {}
    args.update(csrf(request))
    user = User.objects.get(username=user_name)
    if request.method == 'POST':
        user = User.objects.get(username=user_name)
        user = UserProfile.objects.get(user=user)
        rate = request.POST.get('rate','')
        user.borrow_credit += int(rate)
        user.save()
        n = Notification.objects.get(id=notification_id)
        n.viewed = True
        n.save()
        return render_to_response('thankyou.html')

    else:
        args['user'] = user
        args['notification_id'] = notification_id
        return render_to_response('ratepage.html', args)
    