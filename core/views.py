from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
    else:
        form = RegistrationForm()
        
    return render(request, "registration/sign_up.html", {"form": form})


def student_portal(request):
    return render(request, "core/student-portal.html")
