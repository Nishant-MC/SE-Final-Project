from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

#message handler
from django.contrib import messages

from .forms import AddInventoryForm
# Create your views here.


def inventory(request):
    return render_to_response("inventory.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )


def additem(request):
    
    form = AddInventoryForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
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
    