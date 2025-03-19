from email import message
from enum import member
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from .forms import SignInModelForm, LoginForm,EditProfileModelForm
from .models import User,FriendshipModel
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin # if: user is login show the page else: redirect user to login page.
from django.http import Http404
from django.views.generic.edit import UpdateView
from django.db.models import Q

# send email function
from django.core.mail import EmailMessage 
from django.template.loader import render_to_string
import asyncio
from asgiref.sync import async_to_sync
# custom MIXIN for CBV(class base view): redirect to dashbord of user is logined.
from django.contrib.auth.mixins import AccessMixin

class RedirectAuthenticatedUserMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('dashbord-allprojects'))
        return super().dispatch(request, *args, **kwargs)

async def activeEmail(activeCode,to,current_domain):
    context = {
        'subject':'active email',
        'desc':'you can active your account with press buttom button.',
        'link':f"{current_domain}{reverse('account-activeAccount',kwargs={"active_code":activeCode})}"
    }
    message_body =  render_to_string('activeEmail.html',context)
    print(message_body)
    message = EmailMessage("active email",message_body,"udo46133@gmail.com",[to])
    message.content_subtype = 'html'
    try:
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, message.send)
    except Exception as e:
        print(f"except from active email:{e}") 


class Login(RedirectAuthenticatedUserMixin,View):
    def get(self,request):
        form = LoginForm()
        context = {
            'form':form
        }
        return render(request,'login.html',context)

    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user : User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                if not user.is_active:
                    messages.add_message(request,messages.INFO,"your account is not active, please check your inbox and active account.")
                else: 
                    is_paassword_currect = user.check_password(password)
                    if is_paassword_currect:
                        login(request,user)
                        messages.add_message(request,messages.INFO,"login successfuly")
                        return redirect(reverse('home-index'))
                    else:
                        form.add_error('password','password is not valid!')

        context = {
            'form':form
        }
        return render(request,'login.html',context)


class Signup(RedirectAuthenticatedUserMixin,View):
    def get(self,request):
        form = SignInModelForm()
        context = {
            'form' : form
        }
        return render(request,'signup.html',context) 

    def post(self,request):
        form = SignInModelForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data.get('email')
            user_password = form.cleaned_data.get('password')
            user : bool = User.objects.filter(email__iexact=user_email).exists()
            if user : 
                form.add_error('email','email are exist!')
            else : 
                new_user = User(
                    first_name = form.cleaned_data.get('first_name'),
                    last_name = form.cleaned_data.get('last_name'),
                    username = form.cleaned_data.get('username'),
                    Rating = 0, 
                    email=user_email,
                    ActiveCode = get_random_string(length=72),
                    is_active=False
                )
                new_user.set_password(user_password)
                new_user.save()
                async_to_sync(activeEmail)(new_user.get_active_code(), new_user.get_email(), request.build_absolute_uri('/'))
                return redirect(reverse('account-login'))
        context = {
            'form':form
        }
        return render(request,'signup.html',context)


class Profile(LoginRequiredMixin,DetailView):
    template_name = 'profile.html' 
    model = User 
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = self.object.taskMember.all()
        context['projects'] = self.object.projectMember.all()
        context['countProjects'] = context['projects'].filter(Status='done').count()
        result = context['tasks'].filter(Status='done').count() / context['tasks'].count()
        context['taskPercent'] = round(result,1)
        return context


class ActiveAccount(View):
    def get(self,request,active_code):
        user : User = User.objects.filter(ActiveCode__iexact=active_code).first()
        if user is not None : 
            if user.is_active == False:
                user.is_active = True
                user.ActiveCode = get_random_string(72)
                user.save()
                messages.add_message(request,messages.SUCCESS,"your account is actived")
                return redirect(reverse('account-login'))
            else:
                messages.add_message(request,messages.ERROR,"something went wrong")
                return redirect(reverse('account-login')) 
        raise Http404


class EditProfile(View):
    def get(self,request):
        current_user = User.objects.filter(id=request.user.id).first()
        if current_user:
            form = EditProfileModelForm(instance=current_user)
            context = {
                'form':form,
                'user':current_user,
            }
            return render(request,'editProfile.html',context)
        else:
            return redirect(reverse('account-login'))

    def post(self,request):
        current_user = User.objects.filter(id=request.user.id).first()
        form = EditProfileModelForm(request.POST,request.FILES,instance=current_user)
        if form.is_valid():
            form.save(commit=True)
            messages.add_message(request,messages.SUCCESS,"your profile edited")
            return redirect(reverse('account-profile',kwargs={'slug':current_user.slug}))
        context = {
            'form':form,
            'user':current_user,
        }
        return render(request,'editProfile.html',context)



class LogoutView(View):
    def get(self,request):
        logout(request) 
        messages.add_message(request,messages.SUCCESS,"logout successfuly")
        return redirect(reverse('account-login'))



# INFO : partial components.

def accountBar(request):
    current_user = User.objects.filter(id=request.user.id).first() 
    context = {
        'user':current_user
    }
    return render(request,'accountbar.html',context)


def indexAccountBar(request):
    current_user = User.objects.filter(id=request.user.id).first() 
    context = {
        'user':current_user
    }
    return render(request,'indexAccountbar.html',context)


def getFriend(request):
    query = request.GET.get('q','').strip()
    members = ""
    if query:  
        members = User.objects.filter(username__icontains=query)

    context = {
        'members':members,
        'user':request.user.id
    }
    return render(request, "friendship.html",context)

def sendRequest(request,username):
    current_user = User.objects.filter(id=request.user.id).first()
    requested_user = User.objects.filter(username__iexact=username).first()
    friendRequest = FriendshipModel()

    try:
        friendRequest.user1 = current_user
        friendRequest.user2 = requested_user
        friendRequest.save()
        messages.add_message(request,messages.SUCCESS,"your request sended")
    except Exception as e:
        print(e)
        messages.add_message(request,messages.ERROR,"something went wrong")

    return redirect(reverse('account-request'))

def myRequest(request):
    user = User.objects.filter(id=request.user.id).first()
    user_request = FriendshipModel.objects.filter(Q(user2=user) & Q(is_accepted=False)).all()
    context = {
        'requests' : user_request
    }
    return render(request,'all_request.html',context)


def requestRespose(request,request_code,action):
    current_request = FriendshipModel.objects.filter(request_code__iexact=request_code).first()
    if action == "1" :
        current_request.is_accepted = True
        current_request.request_code = get_random_string(30)
        current_request.save()
        messages.add_message(request,messages.SUCCESS,"you accept the request")
        return redirect(reverse('account-myrequest'))
    elif action == "0" : 
        current_request.is_accepted = False 
        current_request.request_code = get_random_string(30)
        current_request.save()
        messages.add_message(request,messages.SUCCESS,"you cancel the request")
        return redirect(reverse('account-myrequest'))
    else:
        messages.add_message(request,messages.ERROR,"something went wrong")
        return redirect(reverse('account-myrequest'))
