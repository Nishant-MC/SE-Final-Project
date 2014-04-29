from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

#message handler
from django.contrib import messages

from .forms import SignUpForm
# Create your views here.


def home(request):
    '''
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        messages.success(request, 'Thank you for signing up!')
        return HttpResponseRedirect('/thank-you/')
       ''' 
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