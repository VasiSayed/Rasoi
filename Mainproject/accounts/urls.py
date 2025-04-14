from django.urls import path
from .views import RegisterView, LoginView,Viewlogout

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),  # User Registration
    path("login/", LoginView.as_view(), name="login"),  # User Login
    path("logout/", Viewlogout.as_view(), name="logout"),  # Logout and Redirect to Login
]
