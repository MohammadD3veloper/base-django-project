from django.contrib.auth import views
from . import views as _
from django.urls import path


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="registration/logout.html"), name='logout'),
    path('signup/',_.signup, name="signup"),
    path('password_change/', views.PasswordChangeView.as_view(template_name="password_change.html"), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(template_name="password_change_done.html"), name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(template_name="password_reset.html"), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(template_name="password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(template_name="password_reset_token.html"), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), name='password_reset_complete'),
]
