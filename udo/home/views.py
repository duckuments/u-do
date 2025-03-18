from django.shortcuts import redirect, render, reverse
from django.views import View
from .forms import ContactModelForm
from django.contrib import messages


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def faq(request):
    return render(request,'faq.html')

def privacy(request):
    return render(request,'privacy.html')

class ContactView(View):
    def get(self,request):

        form = ContactModelForm() 

        data = {
            "forms" : form
        }
        return render(request,'contact.html',data) 

    def post(self,request):
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,"your message sends to our team!")
            return redirect(reverse('home-index'))
        data = { 
            "form" : form
        }
        messages.error(request,"")
        return render(request,'contact.html',data)

def document(request):
    return render(request,'document.html')
