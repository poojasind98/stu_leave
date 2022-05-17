from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.home,name ='home'),
    path('leave_apply',views.leave_apply, name='leave_apply'),
    path('leave_detial/<int:id>',views.leave_detial,name='leave_detail'),
    path('leave_decision/<int:id>',views.leave_decision,name='leave_decision'),
]
