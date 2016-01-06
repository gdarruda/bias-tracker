from django.conf.urls import url
from graphs import views

urlpatterns = [
    url(r'^$', views.index),
]
