from django.conf.urls import url
from . import views


app_name = 'about'

urlpatterns = [

    # start page
    url(r'^$', views.Main.as_view(), name='home'),

]
