from django.db import models
from django.db.models.query_utils import select_related_descend
from django.urls import reverse
from django.utils.text import slugify


STATUS_CHICES = [
    ('not_started','Not Started'),
    ('in_progress','In Progress'),
    ('done','Done')
]

class Category(models.Model):
    Title = models.CharField(max_length=300)

    def __str__(self):
        return self.Title 


class ProjectModel(models.Model):
    Name = models.CharField(max_length=300)
    Description = models.TextField()
    CreateDate = models.DateField(auto_now_add=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.CharField(max_length=20,choices=STATUS_CHICES,default='not_started')
    slug = models.SlugField(default="",null=False)

    # relationships :
    Members = models.ManyToManyField('account.User',related_name="projectMember")
    Admin = models.ManyToManyField('account.User',related_name="admin")

    def get_absolute_url(self):
        return reverse('dashbord-projectdetail',args=[self.slug]) 

    def save(self,*args,**kwargs):
        self.Slug = slugify(self.Name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.Name


class TaskModel(models.Model):
    Title = models.CharField(max_length=200)
    Description = models.TextField()
    CreateDate = models.DateField(auto_now_add=True)
    StartDate = models.DateField()
    EndDate = models.DateField()
    Status = models.CharField(max_length=20,choices=STATUS_CHICES,default='not_started')
    
    # relationships :
    ParentProject = models.ForeignKey(ProjectModel,on_delete=models.CASCADE,related_name="tasks")
    Members = models.ManyToManyField('account.User',related_name="taskMember")
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="category",null=True)
    Admin = models.ManyToManyField('account.User',related_name="taskAdmin")

    slug = models.SlugField(default="",null=False)
    def get_absolute_url(self):
        return reverse('dashbord-taskdetail',args=[self.slug]) 

    def save(self,*args,**kwargs):
        self.slug = slugify(self.Title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.Title
