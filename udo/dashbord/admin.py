from django.contrib import admin
from . import models

admin.site.register(models.ProjectModel)
admin.site.register(models.TaskModel)
admin.site.register(models.Category)
