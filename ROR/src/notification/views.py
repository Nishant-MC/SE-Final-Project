from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from models import Notification
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.context_processors import csrf
# Create your views here.

def show_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    return render_to_response('notification.html', {'notification':n})



def delete_notification(request, notification_id):
    n = Notification.objects.get(id=notification_id)
    n.viewed = True
    n.save()
    return HttpResponseRedirect('/')

def request_item(request, user_name=''):
    
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = user_name)
    title = 'Request from %s'%str(request.user)
    message="I need your item! :)"
    Notification.objects.create(user=name, title=title, message=message, sender=request.user)
    args['name'] = name
    args['user_name'] = user_name
    
    return render_to_response('request_success.html',args)
    
def accept(request, receiver=''):
    
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = receiver)
    title = 'Accept from %s'%str(request.user)
    message="You can pick it up soon! :)"
    Notification.objects.create(user=name, title=title, message=message, sender=request.user)
    args['name'] = name
    args['user_name'] = receiver
    
    return render_to_response('request_success.html',args)
    
    
def deny(request, receiver=''):
    
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = receiver)
    title = 'Deny from %s'%str(request.user)
    message="Sorry! It's not available at the moment!"
    Notification.objects.create(user=name, title=title, message=message, sender=request.user)
    args['name'] = name
    args['user_name'] = receiver
    
    return render_to_response('request_success.html',args)
    
       
    