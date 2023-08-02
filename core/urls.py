from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.LikePost, name='likepost'),
    path('upload', views.upload, name='upload'),
    path('logout', views.logout, name='logout'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('user_comment', views.user_comment, name = 'user_comment'),
    path('repost', views.repost, name = 'repost'),
]
