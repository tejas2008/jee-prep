from django.conf.urls import url
from hotelbooking import views
urlpatterns=[ url(r'^$',views.Hello1,name='Hello1'), ]