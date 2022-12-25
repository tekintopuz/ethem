from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

from .models import userRole


# Create your views here.

def index(request):
    return render(request, "index.html")


def loginViews(request):
    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect("welcome")

    else:

        print("Hata----")

    return render(request, "accounts/login.html", {"form": form})


def registerViews(request):
    form = RegisterForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        name = form.cleaned_data["name"]
        lastname = form.cleaned_data["lastname"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        confPassword = form.cleaned_data["confPassword"]
        userrole = form.cleaned_data["user_role"]

        print(userrole)
        if password == confPassword:
            user = User.objects.create_user(username=username,
                                            first_name=name,
                                            last_name=lastname,
                                            email=email,
                                            password=password)
            user.save()

            userRole_ = userRole(user_role=userrole, userName=username)

            userRole_.save()

            print("Başarili---------------")
            return redirect("loginViews")
        else:
            print("şifreler eşleşmiyor.")

    else:
        print("Register Error!!!!!")

    return render(request, "accounts/register.html", {"form": form})


@login_required(login_url='/login/')
def logoutViews(request):
    logout(request)

    return redirect("index")


@login_required(login_url='/login/')
def welcome(request):
    return render(request, "myApp/welcome.html")


@login_required(login_url='/login/')
def profile(request, userName):
    try:
        user = User.objects.get(username=userName)
        userRole_ = userRole.objects.get(userName=userName)
        info = {"firsName": user.first_name,
                "lastName": user.last_name,
                "mail": user.email,
                "username": user.username,
                "role": userRole_.user_role}


    except:
        return redirect("index")

    return render(request, "accounts/profile.html", {"userName": userName, "info": info})


@login_required(login_url='/login/')
def createPost(request):
    if request.method == "POST":
        title = request.POST.get("create-post-title")

        content = request.POST.get("create-post-content")

        print("-----------------------------")
        print(title)
        print("-----------------------------")
        print(content)
        print("-----------------------------")

    return render(request, "myApp/create-post.html")
