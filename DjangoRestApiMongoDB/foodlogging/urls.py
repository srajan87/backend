from django.conf.urls import url 
from foodlogging import views 
 
urlpatterns = [ 
    url(r'^api/foodlogs$', views.foodlogs_list),
    url(r'^api/foodlogs/(?P<pk>[0-9]+)$', views.foodlogs_detail),
    #url(r'^api/foodlogs/published$', views.tutorial_list_published)
]