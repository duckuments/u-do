from django import forms
from django.forms import fields
from account.models import User

# TODO : fix style.

class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
        "placeholder" : "email"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
        "placeholder" : "password"
    }))


class SignInModelForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
        "placeholder" : "confirm password"
    }))
    class Meta : 
        model = User
        fields = ['first_name','last_name','email','username','password']
        widgets = { 
            "first_name" : forms.TextInput(attrs={
                "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "firstname"
            }),
            "last_name" : forms.TextInput(attrs={
                "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "lastname"
            }),
            "email" : forms.EmailInput(attrs={
                "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "email" 
            }), 
            "username" : forms.TextInput(attrs={
                "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "username"
            }), 
            "password" : forms.PasswordInput(attrs={
                "class" :"input input-bordered w-full xl:max-w-xs lg:max-w-xs md:max-w-md sm:max-w-sm max-w-sm border-neutral bg-primary rounded-none",
                "placeholder" : "password",
            }),
        }
        help_texts = {
            'username' : 'Letters, digits and ./_ only.',
            'password':'Letters, digits and @/./+/-/_ only.'
        }
    def clean(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            self.add_error('confirm_password','confirm password is not matched with password!') 
        return super().clean()


class EditProfileModelForm(forms.ModelForm):
    class Meta : 
        model = User
        fields = ["first_name","last_name","Information","username","ImgName"]
        widgets = { 
            "ImgName" : forms.FileInput(attrs={
                "class":"file-input border-neutral file-input-xs",
            }),
            "first_name" : forms.TextInput(attrs={
                "class" :"w-full bg-primary border-neutral border rounded-none p-2",
            }),
            "last_name" : forms.TextInput(attrs={
                "class" :"w-full bg-primary border-neutral border rounded-none p-2",
            }), 
            "username" : forms.TextInput(attrs={
                "class" :"w-full bg-primary border-neutral border rounded-none p-2",
            }), 
            "Information" : forms.Textarea(attrs={
                "class" :"textarea bg-primary rounded-none border border-neutral w-full",
                "rows": 5,
                "cols": 0
            }),
        }

