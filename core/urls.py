from django.urls import path
from .views import Tasklist,createtask,taskdetail


urlpatterns=[
    path('',Tasklist.as_view()),
    path('Task/<int:pk>/',taskdetail.as_view(),name='taskdetail'),
    path('task-create/',createtask.as_view(),name='Createtask'),
]
