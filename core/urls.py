from django.urls import path
from .views import Tasklist,createtask,taskdetail,Updatetask,delettask,UserLogin,LogoutView,RegisterPage


urlpatterns=[
    path('login/', UserLogin.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('',Tasklist.as_view(),name='tasklist'),
    path('Task/<int:pk>/',taskdetail.as_view(),name='taskdetail'),
    path('task-create/',createtask.as_view(),name='Createtask'),
    path('update-task/<int:pk>',Updatetask.as_view(),name='updatetask'),
    path('delete-task/<int:pk>',delettask.as_view(),name='deletetask'),
]
