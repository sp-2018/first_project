
from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # Root route
    url(r'^process/register$', views.registerUser),
    url(r'^process/login$', views.loginUser),
    url(r'^success$', views.success),
    url(r'^process/logout$', views.logout)
]
