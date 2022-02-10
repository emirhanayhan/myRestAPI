from django.urls import path
from . import views as api_views

urlpatterns = [
    path('user/', api_views.user_list_create_api_view, name='userList'),
    path('user/<int:pk>', api_views.user_detail_api_view, name='user-detail'),
    path('trip/', api_views.usertrip_list_create_api_view, name='triplist'),
    path('trip/<int:pk>', api_views.usertrip_detail_api_view, name='trip-detail'),
    path('tripwithuserid/<int:userid>', api_views.usertripwithuserid_detail_api_view, name='trip-detailwithuserid'),
]
