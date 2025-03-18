from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Login.as_view(),name='account-login'),
    path('signup/',views.Signup.as_view(),name='account-signup'),
    path('profile/<slug:slug>',views.Profile.as_view(),name='account-profile'),
    path('active-account/<active_code>',views.ActiveAccount.as_view(),name='account-activeAccount'),
    path('editprofile/',views.EditProfile.as_view(),name="account-editProfile"),
    path('logout/',views.LogoutView.as_view(),name="account-logout")
]
