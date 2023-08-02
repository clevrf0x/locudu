from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.db.models import Q
from .models import User
from .utils import normalize_phone_number, normalize_email


# TODO: Handle case where users are already authenticated
# TODO: Handle user verified or not
class LoginView(View):
    def get(self, request):
        return render(request, "users/login.html")

    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not (username and password):
            messages.error(request, "Username or password missing")
            return redirect("login")

        user = authenticate(username=username, password=password)

        if not user:
            messages.error(request, "Invalid Credentials")
            return redirect("login")

        login(request, user)
        messages.info(request, "Login Successful")
        return redirect("/")


class RegisterView(View):
    def get(self, request):
        return render(request, "users/register.html")

    # TODO: Send Verification OTP
    # TODO: Implement strong password validations (client-side)
    def post(self, request):
        full_name = request.POST.get("full_name")
        phone_number = normalize_phone_number(request.POST.get("phone_number"))
        email = normalize_email(request.POST.get("email"))
        password = request.POST.get("password")

        if not (full_name and phone_number and password):
            messages.error(request, "Missing required fields")
            return redirect("register")

        # Check if user already exists or not
        query = Q(phone_number=phone_number)
        if email:
            query = Q(phone_number=phone_number) | Q(email=email)
            
        user = User.objects.filter(query)
        if user:
            messages.error(request, "User already exists")
            return redirect("register")

        user = User.objects.create_user(phone_number, full_name, password)
        user.email = email
        user.bio = request.POST.get("bio")
        user.pincode = request.POST.get("pincode")
        user.city = request.POST.get("city")
        user.district = request.POST.get("district")
        user.state = request.POST.get("state")
        user.save()

        messages.success(request, "User created successfully")
        return redirect("login")


class LogoutView(View):
    def get(self, request):
        messages.info(request, "Logout Successful")
        logout(request)
        return redirect("login")
