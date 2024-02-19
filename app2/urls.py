#To create specific urls we need to import path function from django.urls and views from app

from django.urls import path
from .views import *

#app_name can be any name,this will be used in the time url navigation
app_name='specific'


#create urlpatterns for paths or urls
urlpatterns=[
    path('render_html2/',render_html2,name='render_html2'),
    path('http_Response/',http_Response,name='http_Response'),


]