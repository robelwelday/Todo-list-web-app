from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Task
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView ,DeleteView
from django.urls import reverse_lazy


class Tasklist(ListView):
    model=Task
    template_name='task_list.html'    
    context_object_name='tasks'

class taskdetail(DetailView):
    model=Task
    template_name='task_detail.html'
    context_object_name='t_detail'
class createtask(CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ['user', 'taskname', 'description', 'completed']  # Ensure these fields exist in the Task model
    success_url = reverse_lazy('tasklist') 
    
class Updatetask(UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = ['user', 'taskname', 'description', 'completed']  # Ensure these fields exist in the Task model
    success_url = reverse_lazy('tasklist') # Ensure 'tasklist' is correctly defined in core/urls.py


class delettask(DeleteView):
    model=Task

