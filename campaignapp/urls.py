from django.urls import path
from . import views

urlpatterns = [
	path('hello/', views.say_hello, name='index'),
	path('user/<str:id>', views.get_user, name='get_user'),
	path('csrftoken', views.get_token, name='get_token'),
	path('addcampaign', views.add_campaign, name='add_campaign'),
	path('allcampaign', views.get_all_campaign, name='get_all_campaign'),
	path('campaignbyuserid/<str:user_id>', views.get_campaign_by_user_id, name='get_campaign_by_user_id'),
	path('editcampaign/<str:campaign_id>', views.edit_campaign, name='edit_campaign'),
	path('deletecampaign/<str:campaign_id>', views.delete_campaign, name='delete_campaign'),
]
