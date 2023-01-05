from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.say_hello, name='index'),
	path('user/<str:id>', views.get_user, name='get_user'),
	path('addcampaign', views.add_campaign, name='add_campaign'),
]
