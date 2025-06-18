from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Task
from django.views.generic import DetailView
from django.views.generic.edit import CreateView,UpdateView ,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

class UserLogin(LoginView):
        template_name = 'login.html'
        fields='__all__'
        redirect_authenticated_user=True
        def get_success_url(self):
             return reverse_lazy('tasklist')

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



class UserLogoutView(LogoutView):
        next_page = reverse_lazy('tasklist')  # Redirect after logout

class UserRegisterView(FormView):
        template_name = 'register.html'
        form_class = UserCreationForm
        success_url = reverse_lazy('tasklist')

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)

class delettask(DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasklist')
    template_name='delete_task.html'
