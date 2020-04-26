from django.urls import path
from smc_app import views

app_name = 'smc_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('m/',views.majju,name='majju'),
    path('s/',views.sallu,name='sallu'),
]
