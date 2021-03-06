from django.conf.urls import patterns, url

urlpatterns = patterns('notification.views',
                       
                       url(r'^show/(?P<notification_id>\d+)/$', 'show_notification'),
                       
                       url(r'^delete/(?P<notification_id>\d+)/$', 'delete_notification'),
                       
                       url(r'^request/(?P<item_id>\d+)/$', 'request_page', name='request_page'),
                       
                       url(r'^request_send/(?P<lender>\w+)/(?P<item_id>\d+)/$', 'request_item', name='request_item'),
                       
                       url(r'^accept/(?P<receiver>\w+)/(?P<item_id>\d+)/(?P<notification_id>\d+)/$', 'accept', name='accept'),
                       
                       url(r'^deny/(?P<receiver>\w+)/(?P<notification_id>\d+)/$', 'deny', name='deny'),
                       
                       url(r'^inbox/(?P<option>\w+)/$', 'inbox', name='inbox'),
                       
                       url(r'^rate/(?P<user_name>\w+)/(?P<notification_id>\d+)/$', 'rate', name='rate'),
                      )
