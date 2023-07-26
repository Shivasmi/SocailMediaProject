from django.urls import path
from . import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.LikePost, name='likepost'),
    path('follow', views.follow, name='follow'),
    path('logout', views.logout, name='logout'),
    path('personal_info', views.personal_info, name='personal_info'),
   
]
