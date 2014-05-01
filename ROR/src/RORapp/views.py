from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from forms import MyRegistrationForm

### Home View ###

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
    
    user= str(request.user)
    if user == 'AnonymousUser':
        user = None
    args['user_name'] = user
    
    
    '''
    if request.user.is_authenticated():
        return HttpResponse("%s is logged in" % user_str)
    else:
        return HttpResponse("not logged in")
    '''
    return render_to_response("home.html",
                              args, context_instance=RequestContext(request))
                              #locals(),
                              #context_instance=RequestContext(request)
                              #)
    



### LOGIN ###
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')
    
def loggedin(request):
    
    return render_to_response('loggedin.html', {'full_name': request.user.username, 'user_name':request.user.username})

def invalid_login(request):
    return render_to_response('login_invalid.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    #return render_to_response('logout.html')

### REGISTRATION ###

def register_user(request):
    if request.method == 'POST':
        form_register = MyRegistrationForm(request.POST)
        if form_register.is_valid():
            form_register.save()
            return HttpResponseRedirect('/accounts/register_success')
        
        else:
            return HttpResponseRedirect('/accounts/register_fail')
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = MyRegistrationForm()
    print args
    return render_to_response('home.html',args)

def register_success(request):
    return render_to_response('register_success.html')

def register_fail(request):
    return render_to_response('register_fail.html')

def viewfriend(request):
    users = User.objects.all()
    args= {}
    args.update(csrf(request))
    
    args['users'] = users
    
    return render_to_response('viewfriend.html',args)
    
    