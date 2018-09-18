from django.conf.urls import url
from .import views
# from basic_app import views

######################
## Template Tagging ##
######################

app_name = 'basic_app'

urlpatterns= [
    # url(r'^relative/$',views.relative,name='relative'),
    # url(r'^other/$',views.other,name='other'),

    url('relative/',views.relative,name='relative'),
    url('other/',views.other,name='other'),    
]
