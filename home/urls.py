from django.conf.urls import url
from . import views


urlpatterns = [

    # start page
    url(r'', views.Home.as_view(), name='home'),

]
