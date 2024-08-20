from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('profile', views.profile_view, name = 'profile'),
    path('logout/', views.LogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
    path('register', views.register, name = 'register')

]
