from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from forms import MyRegistrationForm
from inventory.models import Item
from notification.models import Notification
from django.contrib.auth.decorators import login_required
### Home View ###

@login_required(login_url='/accounts/login')
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
    n = Notification.objects.filter(user=request.user, viewed=False)
    return HttpResponseRedirect('/inventory/all')
    #return render_to_response('loggedin.html',
     #                         {'full_name': request.user.username, 'user_name':request.user.username, 'notifications':n}
      #                        )

def invalid_login(request):
    return render_to_response('login_invalid.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    #return render_to_response('logout.html')

### REGISTRATION ###

def register_user(request):
    if request.method == 'POST':
        first_name=request.POST.get('first_name','')
        last_name=request.POST.get('last_name','')
        username=request.POST.get('user_name','')
        password1=request.POST.get('password1','')
        password2=request.POST.get('password2','')
        email=request.POST.get('email','')
        if password1 != password2 or username=='' or email=='':
            return HttpResponseRedirect('/accounts/register_fail')
        else:
            try:
                user = User.objects.create_user(username = username, email = email, password = password1)
            except:
                return HttpResponseRedirect('/accounts/register_fail')                
            user.first_name =  first_name
            user.last_name = last_name
            user.save()
            return HttpResponseRedirect('/accounts/register_success')
    
    args = {}
    args.update(csrf(request))
    '''
    args['form'] = MyRegistrationForm()
    print args
    '''
    return render_to_response('register.html',args)

def register_success(request):
    return render_to_response('register_success.html')

def register_fail(request):
    return render_to_response('register_fail.html')

def viewfriend(request):
    user = str(request.user)
    if user == 'AnonymousUser':
        user = None
    
    users = User.objects.all()
    args= {}
    args.update(csrf(request))
    args['user_name'] = user
    args['users'] = users
    
    return render_to_response('viewfriend.html',args)
    
def viewuserinv(request, user_name=''):
    
    args = {}
    args.update(csrf(request))
    name = User.objects.get(username = user_name)
    items = Item.objects.filter(owner__exact=name)
    args['items'] = items
    args['user_name'] = user_name
    args['loggedin_user'] = str(request.user)
    
    
    
    return render_to_response("inventory.html",
                              args,
                              context_instance=RequestContext(request)
                              )
    
    
    
    
    
    
    
    
    
    
  