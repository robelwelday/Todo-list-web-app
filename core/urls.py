from django.urls import path
from .views import Tasklist,createtask,taskdetail,Updatetask,delettask


urlpatterns=[
    path('',Tasklist.as_view(),name='tasklist'),
    path('Task/<int:pk>/',taskdetail.as_view(),name='taskdetail'),
    path('task-create/',createtask.as_view(),name='Createtask'),
    path('update-task/<int:pk>',Updatetask.as_view(),name='updatetask'),
    path('delete-task/<int:pk>',delettask.as_view(),name='deletetask'),
]
