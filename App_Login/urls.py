from django.urls import path
from . import views

app_name = 'App_Login'

urlpatterns = [ 
  path('signup/',views.sign_up,name='signup'),
  path('signin/',views.login_page,name='signin'),
  path('logout/',views.logout_user,name='logout'),
  path('profile/',views.profile_page,name='profile'),
  path('change_profile',views.user_change,name='change_profile'),
  path('password/',views.pass_change,name='pass_change'),
  path('profile_update/',views.add_pro_pic,name='profile_update'),
  path('change-picture/',views.change_pro_pic,name='change_pro_picture'),
]
