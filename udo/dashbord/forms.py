from django import forms
from . import models
from account.models import FriendshipModel

class ProjectModelForm(forms.ModelForm):
    class Meta : 
        model = models.ProjectModel
        fields = "__all__"
        widgets = {
            "Name":forms.TextInput(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Description":forms.Textarea(attrs={
                "class" :"textarea bg-primary rounded-none border border-neutral w-full",
            }),
            "StartDate":forms.SelectDateWidget(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "EndDate":forms.SelectDateWidget(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Status":forms.Select(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Members":forms.SelectMultiple(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "CreateDate":forms.SelectDateWidget(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "slug":forms.TextInput(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Admin":forms.SelectMultiple(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
        } 
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['Members'].queryset = FriendshipModel.get_friends(user)
            self.fields['Admin'].queryset = FriendshipModel.get_friends(user)

class TaskModelForm(forms.ModelForm):
    class Meta : 
        model = models.TaskModel
        exclude = ["CreateDate"]
        widgets = {
            "Title":forms.TextInput(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Description":forms.Textarea(attrs={
                "class" :"textarea bg-primary rounded-none border border-neutral w-full",
            }),
            "StartDate":forms.SelectDateWidget(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "EndDate":forms.SelectDateWidget(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Status":forms.Select(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Members":forms.SelectMultiple(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "slug":forms.TextInput(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "ParentProject":forms.Select(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Category":forms.Select(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "Admin":forms.SelectMultiple(attrs={
                "class":"w-full bg-primary border-neutral border rounded-none p-2",
            }),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['Members'].queryset = FriendshipModel.get_friends(user)
            self.fields['Admin'].queryset = FriendshipModel.get_friends(user)
