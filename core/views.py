from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "core/index.html")


def signin(request):
    return render(request, "registration/signin.html")


def signup(request):
    return render(request, "registration/signup.html")


def student_portal(request):
    return render(request, "core/student-portal.html")