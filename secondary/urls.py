from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # admin
    path('principal/', views.admin, name='principal'),

    # login page
    path('login/', views.login_page, name='login-page'),

    # logout
    path('logout/', views.logoutUser, name='logout')
]