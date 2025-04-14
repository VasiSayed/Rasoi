from datetime import date, timedelta
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegistrationForm,LoginForm
from django.contrib.auth import authenticate, login,logout
from django.conf import settings

class RegisterView(View):
    def get(self, request):
        form = RegistrationForm()
        title = "Register - Rasoi App"
        return render(request, "accounts/form.html", {"form": form, "title": title})

    def post(self, request,):
        form = RegistrationForm(request.POST)
        title = "Register - Rasoi App"

        if form.is_valid():
            user = form.save(commit=False)
            username = user.username
            email = user.email
            user.save()
            messages.success(request, f"Welcome {username}, your registration is successful! 🎉")
            email_subject = "Welcome to Rasoi App - Your Food Adventure Begins!"
            email_body = f"""
🍽️ Hello {username},

Thank you for signing up with Rasoi App! 🍕🥗  
Your account is now active, and you're ready to explore a world of delicious food.

### What’s Next?
- Browse your favorite cuisines 🥘  
- Order meals from top-rated restaurants 🍔  
- Enjoy fast and easy delivery 🚀  

📢 **Exclusive Offer**: Use code **WELCOME10** for 10% off your first order!  

For assistance, reach out to **support@rasoiapp.com**.  

Bon Appétit!  
**The Rasoi App Team**  
"""

            send_mail(
                email_subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=True,
            )

            return redirect("login")
        else:
            messages.error(request, "Please fill out the form correctly.")
            return render(request, "accounts/form.html", {"form": form, "title": title})



class LoginView(View):
    def get(self, request):
        form = LoginForm()
        title = "Login - Rasoi App"
        return render(request, "accounts/form.html", {"form": form, "title": title})

    def post(self, request):
        form = LoginForm(request.POST)
        title = "Login - Rasoi App"

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}! 🍕")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password. Please try again.")
                return render(request, "accounts/form.html", {"form": form, "title": title})

        messages.error(request, "Please enter valid login details.")
        return render(request, "accounts/form.html", {"form": form, "title": title})



class Viewlogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully!")
        return redirect("login") 