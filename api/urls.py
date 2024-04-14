from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.user_logout, name='logout'),
    path('travel_history/', views.travel_history, name='travel_history'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('saved_locations/', views.saved_locations, name='saved_locations'),
    path('user_list/', views.user_list, name='user_list'),
     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
