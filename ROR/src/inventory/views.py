from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
#message handler
from django.contrib import messages

from .forms import AddInventoryForm
# Create your views here.
from .models import Item

def inventory(request):
    
    args = {}
    args.update(csrf(request))
        
    user= str(request.user)
    if user == 'AnonymousUser':
        user = None
    else:
        items = Item.objects.filter(owner__exact=request.user)
        args['items'] = items
    args['user_name'] = user
    
        
    return render_to_response("inventory.html",
                              args,
                              )


def additem(request):
    
    form = AddInventoryForm(request.POST or None)
    user= request.user
    if form.is_valid():
        save_it = form.save(user, commit=False)
        save_it.save()
        return HttpResponseRedirect('/inventory/add_success')
     
    return render_to_response("additem.html",
                              locals(),
                              context_instance=RequestContext(request)
                             )
                              

def add_success(request):
    return render_to_response("add_success.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )
    
def viewitem(request, item_id=1):
    return render_to_response("item.html",
                              {'item':Item.objects.get(id=item_id)},
                              context_instance=RequestContext(request)
                              )

def removeitem(request, item_id=1):
    item = Item.objects.filter(id=item_id)
    item.delete()
    return HttpResponseRedirect('/inventory/all')

def browseitem(request):
    item = Item.objects.all()
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