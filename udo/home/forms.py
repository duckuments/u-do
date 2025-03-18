from django import forms
from django.forms import EmailInput, TextInput, Textarea
from .models import ContactModel 

class ContactModelForm(forms.ModelForm):
    class Meta : 
        model = ContactModel
        exclude = ["createDate"]
        widgets = { 
            "fullName" : TextInput(attrs={
                "class" :"input input-bordered xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "fullName"
            }),
            "email" : EmailInput(attrs={
                "class" :"input input-bordered xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "email" 
            }), 
            "subject" : TextInput(attrs={
                "class" :"input input-bordered xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "subject"
            }), 
            "message" : Textarea(attrs={
                "class" :"textarea textarea-bordered rounded-none bg-primary p-2 textarea-md xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral",
                "placeholder" : "message",
                "rows": 5,
                "cols": 0
            })
        }
