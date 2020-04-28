from django.urls import path
from smc_app import views

app_name = 'smc_app'

urlpatterns = [
    path('',views.userlogin,name='userlogin'),
    path('m/',views.majju,name='majju'),
    path('s/',views.sallu,name='sallu'),
    path('register/',views.register,name='register'),
    path('user_login/',views.userlogin,name='userlogin'),
    path('user_logout/',views.userlogout,name='userlogout'),
]
