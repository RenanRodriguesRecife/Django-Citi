from django.conf.urls import url
from . import views

ulrpatterns = [
	url(r'^$',views.home, name='home')
]