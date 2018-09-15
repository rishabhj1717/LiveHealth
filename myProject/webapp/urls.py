from django.urls import path,re_path
from django.conf.urls import url,include

from . import views

urlpatterns = [
	path('polls/',views.index,name="index"),
	re_path(r'tp/$',views.detail),
	re_path(r'signup/$',views.signup),
	re_path(r'login/$',views.log_in),
]