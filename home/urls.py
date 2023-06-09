from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('home/', views.HomePageView.as_view(), name='home'),
    path('contact/', views.ContactPageView.as_view(), name='contact'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('thanks/', views.ThanksPageView.as_view(), name='thanks'),
]