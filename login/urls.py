from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [

    # login page
    url('^$', views.Login.as_view(), name='login'),

    # log up page
    url('^registration/$', views.LogUp.as_view(), name='log_up'),

    # log out
    url(r'logout/$', views.LogOut.as_view(), name='logout'),
]