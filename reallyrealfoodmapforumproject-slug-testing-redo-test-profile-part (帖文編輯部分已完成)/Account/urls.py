from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('signin/', views.account_signin_view, name="signin"),
    path('signup/', views.account_signup_view, name="signup"),
]
