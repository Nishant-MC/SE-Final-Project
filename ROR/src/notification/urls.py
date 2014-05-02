from django.conf.urls import patterns, url

urlpatterns = patterns('notification.views',
                       
                       url(r'^show/(?P<notification_id>\d+)/$', 'show_notification'),
                       
                       url(r'^delete/(?P<notification_id>\d+)/$', 'delete_notification'),
                       
                       url(r'^request/(?P<user_name>\w+)/$', 'request_item', name='request_item'),
                       
                       url(r'^accept/(?P<receiver>\w+)/$', 'accept', name='accept'),
                       
                       url(r'^deny/(?P<receiver>\w+)/$', 'deny', name='deny'),
                      )
