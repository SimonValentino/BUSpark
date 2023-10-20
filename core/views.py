from django.shortcuts import render, redirect
from .forms import RegistrationForm, ReviewForm
from django.contrib.auth import login, logout, authenticate
from .models import Review


def index(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            review = form.cleaned_data['review']

            review = Review(username=username, email=email, review=review)
            review.save()

            return redirect("/")
        else:
            return render(request, "core/index.html", {'form': form})
    else:
        form = ReviewForm()

    return render(request, "core/index.html", {"form": form})


def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()

    return render(request, "registration/sign_up.html", {"form": form})


def student_portal(request):
    return render(request, "core/student-portal.html")
