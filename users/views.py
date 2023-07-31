from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View


# TODO: Handle case where users are already authenticated
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


class LogoutView(View):
    def get(self, request):
        messages.info(request, "Logout Successful")
        logout(request)
        return redirect("login")
