from django.http import HttpResponsePermanentRedirect
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="home-index"),
    path('about/',views.about,name="home-about"),
    path('faq/',views.faq,name="home-faq"),
    path('privacy/',views.privacy,name="home-privacy"),
    path('contact/',views.ContactView.as_view(),name="home-contact"),
    path('documnet/',views.document,name="home-document")
]
