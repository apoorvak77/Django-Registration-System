from django.urls import path 
from . import views
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


urlpatterns = [
    path('',views.index, name='index'),
    #path('login/',login, {'template_name':'registerapp/login.html'})
    path('login/', LoginView.as_view(template_name='registerapp/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='registerapp/logout.html'), name="logout"),
    path('register/', views.register , name="register"),
    path('profile/', views.profile , name="profile"),
    path('profile/edit', views.edit_profile , name="edit_profile"),
    path('change_password/', views.change_password , name="change_password"),
    path('reset_password/', PasswordResetView.as_view(), name='reset_password' ),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]