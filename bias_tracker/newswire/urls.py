from django.conf.urls import url
from newswire import views

urlpatterns = [
    url(r'^$', views.index),
]
