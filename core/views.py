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
from django.contrib.auth.mixins import LoginRequiredMixin

class UserLogin(LoginView):
        template_name = 'login.html'
        fields='__all__'
        redirect_authenticated_user=True
        def get_success_url(self):
             return reverse_lazy('tasklist')

class Tasklist(LoginRequiredMixin,ListView):
    model=Task
    template_name='task_list.html'    
    context_object_name='tasks'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context

class taskdetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name='task_detail.html'
    context_object_name='t_detail'
class createtask(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = [ 'taskname', 'description', 'completed']  # Ensure these fields exist in the Task model
    success_url = reverse_lazy('tasklist') 
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(createtask, self).form_valid(form)
    
class Updatetask(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'update_task.html'
    fields = [ 'taskname', 'description', 'completed']  # Ensure these fields exist in the Task model
    success_url = reverse_lazy('tasklist') # Ensure 'tasklist' is correctly defined in core/urls.py
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(createtask, self).form_valid(form)
    
class delettask(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasklist')
    template_name='delete_task.html'

class UserLogoutView(LogoutView):
        next_page = reverse_lazy('tasklist')  # Redirect after logout

class UserRegisterView(FormView):
        template_name = 'register.html'
        form_class = UserCreationForm
        success_url = reverse_lazy('tasklist')

        def form_valid(self, form):
            form.save()
            return super().form_valid(form)


