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
    
    url(r'^inventory/add_success/$', 'inventory.views.add_success', name='addsuccess'),
    # User auth urls
    url(r'^accounts/login/$', 'RORapp.views.login'),
    url(r'^accounts/auth/$', 'RORapp.views.auth_view'),
    url(r'^accounts/logout/$', 'RORapp.views.logout'),
    url(r'^accounts/loggedin/$', 'RORapp.views.loggedin'),
    url(r'^accounts/invalid/$', 'RORapp.views.invalid_login'),    
    
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
    
    
    

    
