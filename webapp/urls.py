
from django.conf.urls import url

from webapp.views import demo

urlpatterns = [
    url(r'^$', demo.index),
]
