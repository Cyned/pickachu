from django.conf.urls import url
from . import views


app_name = 'home'

urlpatterns = [

    # start page
    url(r'^$', views.Home.as_view(), name='home'),

]
