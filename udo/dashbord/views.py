from django.shortcuts import redirect, render
from django.views.generic import DetailView,CreateView,ListView, UpdateView
from django.urls import reverse
from .models import ProjectModel, TaskModel
from django.contrib.auth.mixins import LoginRequiredMixin # if: user is login show the page else: redirect user to login page.
from .forms import ProjectModelForm, TaskModelForm
from django.db.models import Q
from django.utils.text import slugify
from django.contrib import messages

class AllProjects(LoginRequiredMixin,ListView):
    login_url = '/account/login/' 
    redirect_field_name = 'next'
    template_name = "allProjects.html"
    model = ProjectModel
    context_object_name = 'projects'

    def get_queryset(self):
        user = self.request.user
        return ProjectModel.objects.filter(Q(Members=user) | Q(Admin=user))


class AllTasks(LoginRequiredMixin,ListView):
    login_url = '/account/login/' 
    redirect_field_name = 'next'
    template_name = "allTasks.html"
    model = TaskModel 
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        return TaskModel.objects.filter(Q(Members=user) | Q(Admin=user))


class ProjectDetail(LoginRequiredMixin,DetailView):
    template_name = 'projectDetail.html' 
    model = ProjectModel
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.tasks.all()
        context['form'] = TaskModelForm() 
        return context

    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if request.user not in project.Admin.all() or request.user not in project.Members.all():
            messages.add_message(request,messages.INFO,"You are not an admin or member.")
            return redirect(reverse('dashbord-allprojects')) 
        return super().dispatch(request, *args, **kwargs)

class TaskDetail(LoginRequiredMixin,DetailView):
    template_name = 'taskDetail.html' 
    model = TaskModel 
    context_object_name = 'task'

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user not in task.Admin.all() or request.user not in task.Members.all():
            messages.add_message(request,messages.INFO,"You are not an admin or member.")
            return redirect(reverse('dashbord-alltask')) 
        return super().dispatch(request, *args, **kwargs)


class CreateNewProject(LoginRequiredMixin,CreateView):
    model = ProjectModel
    template_name = 'newProject.html'
    form_class = ProjectModelForm

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.Name)
        return super().form_valid(form)

class CreateNewTask(LoginRequiredMixin,CreateView):
    model = TaskModel
    template_name = 'newTask.html'
    form_class = TaskModelForm 
 
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.Title)
        return super().form_valid(form)

class EditTaskView(UpdateView):
    template_name = "editTask.html"
    model = TaskModel
    form_class = TaskModelForm
    context_object_name = "task"

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if request.user not in task.Admin.all():
            messages.add_message(request,messages.INFO,"You are not an admin or member.")
            return redirect(reverse('dashbord-alltask')) 
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashbord-alltasks')

class EditProjectView(UpdateView):
    template_name = "editProject.html"
    model = ProjectModel
    form_class = ProjectModelForm
    context_object_name = 'project'


    def dispatch(self, request, *args, **kwargs):
        project = self.get_object()
        if request.user not in project.Admin.all():  # Restrict access
            messages.add_message(request,messages.INFO,"You are not an admin or member.")
            return redirect(reverse('dashbord-allprojects')) 
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('dashbord-allprojects')



