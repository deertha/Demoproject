from django.urls import path
from .views import *

urlpatterns = [
    # path('',index,name='index'),
    
    # path('self/',self1,name='self'),
    # path('context/',basic,name='context'),
    path('',register_view,name='register'),
    path('home1/',home1,name='home1'),
    path('about/',about,name='about'),
    path('con/',create_contact,name='contact'),
    path('base/',base,name='base'),
    # path('booking/',create_todo,name='booking'),
    path('booking1/',bookingss,name='booking'),
    path('doctors/',doctor,name='doctors'),
    # path('department/',departments,name='department'),
    path('cbvhome/',Tasklistviews.as_view(),name='department'),
    path('cbvdetail/<int:pk>',TaskDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>', TaskUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>', TaskDeleteView.as_view(),name='cbvdelete'),
    path('cbvcreate/', EmployeeCreate.as_view(),name='cbvcreate'),
]