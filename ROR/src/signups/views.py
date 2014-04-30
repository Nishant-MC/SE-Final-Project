from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

#message handler
from django.contrib import messages

from django.core.context_processors import csrf
#from .forms import MyRegistrationForm

from .forms import SignUpForm
# Create your views here.


def home(request):
    
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
        else:
            return HttpResponseRedirect('/accounts/register_fail')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    print args
    
    
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )
    

def thankyou(request):
            
    return render_to_response("thankyou.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )

def aboutus(request):
            
    return render_to_response("aboutus.html",
                              locals(),
                              context_instance=RequestContext(request)
                              )