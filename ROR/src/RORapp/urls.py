from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', 'RORapp.views.home', name='home'),
    
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    
    url(r'^about-us/$', 'signups.views.aboutus', name='aboutus'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^inventory/all/$', 'inventory.views.inventory', name='inventory'),
    
    url(r'^inventory/additem/$', 'inventory.views.additem', name='additem'),
    
    url(r'^inventory/get/(?P<item_id>\d+)/$', 'inventory.views.viewitem', name='viewitem'),
    
    url(r'^inventory/remove/(?P<item_id>\d+)/$', 'inventory.views.removeitem', name='removeitem'),
    
    url(r'^browseitem/all/$', 'inventory.views.browseitem', name='browseitem'),
    
    url(r'^viewfriend/all/$', 'RORapp.views.viewfriend', name='viewfriend'),
    
    url(r'^inventory/view/(?P<user_name>\w+)/$', 'RORapp.views.viewuserinv', name='viewuserinv'),
    
    url(r'^inventory/add_success/$', 'inventory.views.add_success', name='addsuccess'),
    # User auth urls
    url(r'^accounts/login/$', 'RORapp.views.login', name='login'),
    url(r'^accounts/auth/$', 'RORapp.views.auth_view', name='auth_view'),
    url(r'^accounts/logout/$', 'RORapp.views.logout', name='logout'),
    url(r'^accounts/loggedin/$', 'RORapp.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'RORapp.views.invalid_login', name='invalidlogin'),    
    
    # User registration
    url(r'^accounts/register/$', 'RORapp.views.register_user', name="register"),
    url(r'^accounts/register_success/$', 'RORapp.views.register_success', name="register_success"),
    url(r'^accounts/register_fail/$', 'RORapp.views.register_fail', name="register_fail")
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    
    
    

    
