from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
#message handler
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
from .forms import AddInventoryForm
# Create your views here.
from .models import Item
from notification.models import Notification
from django.contrib.auth.decorators import login_required
from userprofile.models import UserProfile

@login_required(login_url='/accounts/login')   # Very useful feature!
def inventory(request):
    args = {}
    args.update(csrf(request))
        
    user= str(request.user)
    if user == 'AnonymousUser':
        user = None
    else:
        n = Notification.objects.filter(receiver=request.user, viewed=False)
        items = Item.objects.filter(owner__exact=request.user)
        args['items'] = items
        args['notifications'] = n
    checked_out_items = Item.objects.filter(available = False, owner = request.user)
    checked_in_items = Item.objects.filter(holder = request.user)
    credit = UserProfile.objects.get(user=request.user)
    args['user'] = request.user
    args['user_name'] = user
    args['loggedin_user'] = user
    args['checked_out_items'] = checked_out_items
    args['checked_in_items'] = checked_in_items
    args['credit'] = credit
    
    #else:
    #    args['loggedin_user'] = login_name
        
    
        
    return render_to_response("inventory.html",
                              args,
                              )


def additem(request):
    if request.method == 'POST':
        form = AddInventoryForm(request.POST , request.FILES)
        user= request.user
        if form.is_valid():
            #save_it = form.save(user, commit=False)
            form.save(user)
            item_num = UserProfile.objects.get(user=user)
            item_num.item_number += 1
            item_num.save()
            return HttpResponseRedirect('/inventory/add_success')
    else:
        form = AddInventoryForm()
    
    args = {}
    args.update(csrf(request))
    args['form'] = form
    
    return render_to_response("additem.html",
                              args,
                              context_instance=RequestContext(request)
                             )
                              

def add_success(request):
    return render_to_response("add_success.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )

    
def viewitem(request, item_id=''):
    args={}
    args.update(csrf(request))
    args['item'] = Item.objects.get(id=item_id)
    args['user_name'] = request.user
    
    return render_to_response("item.html",
                              args,
                              context_instance=RequestContext(request)
                              )


def removeitem(request, item_id=''):
    item = Item.objects.get(id=item_id)
    user = item.owner
    item_num = UserProfile.objects.get(user=user)
    item_num.item_number -= 1
    item_num.save()
    item.delete()
    return HttpResponseRedirect('/inventory/all')

@login_required(login_url='/accounts/login') 
def browseitem(request):
    item = Item.objects.all().exclude(owner=request.user)
    user= str(request.user)
    if user == 'AnonymousUser':
        user = None
    args={}
    args.update(csrf(request))
    args['items'] = item
    args['user_name'] = user
    return render_to_response("browseitem.html",
                              args,
                              context_instance=RequestContext(request)
                             )

def return_item(request, item_id=''):
    
    
    item = Item.objects.get(id=item_id)
    item.available=True
    item.holder = None
    item.due_date = None
    item.checked_out_date= None
    item.save()
    borrower = UserProfile.objects.get(user=request.user)
    borrower.borrow_credit+=1
    borrower.save()
    lender = UserProfile.objects.get(user=item.owner)
    lender.lend_credit+=1
    lender.save()
    
    title = 'Return: %s'%item.item_name
    message='Thank you for lending me your %s. Please take time to rate me as a borrower!'%item.item_name
    expiry_day = datetime.now() + timedelta(days=30)
    Notification.objects.create(item=None, receiver=lender.user, title=title, message=message, sender=request.user, m_type = 'response', expiry_day=expiry_day, status='return')
    
    
    
    return HttpResponseRedirect('/inventory/all')





