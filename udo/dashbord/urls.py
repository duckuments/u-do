from django.urls import path
from . import views


urlpatterns = [
    path('allprojects/',views.AllProjects.as_view(),name='dashbord-allprojects'),
    path('alltasks/',views.AllTasks.as_view(),name='dashbord-alltasks'),
    path('projectdetail/<slug:slug>',views.ProjectDetail.as_view(),name="dashbord-projectdetail"),
    path('taskdetail/<slug:slug>',views.TaskDetail.as_view(),name='dashbord-taskdetail'),
    path('new-project/',views.CreateNewProject.as_view(),name='dashbord-newProject'),
    path('new-task/',views.CreateNewTask.as_view(),name='dashbord-newTask'),
    path('edit-task/<slug:slug>',views.EditTaskView.as_view(),name='dashbord-editTask'),
    path('edit-project/<slug:slug>',views.EditProjectView.as_view(),name='dashbord-editProject'),
]
