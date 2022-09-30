from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.html import strip_tags
from .models import *
from .forms import *

# Create your views here.
def index(request):
    reviews = Review.objects.all().order_by("-id")
    messages_count = Message.objects.all().count()
    reviews_count = Review.objects.all().count()
    context = {
        'messages_count':messages_count,
        'reviews_count':reviews_count,
        'reviews':reviews
    }
    return render(request, 'index.html', context)

# ******************* SEND VIEW *****************************
def send(request):
    if request.method =='POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message successfully sent")
            return redirect(request.META.get("HTTP_REFERER"))

        else:
            for field, error in form.errors.items():
                error = strip_tags(error)
                messages.error(request,f"{field}: {error}")
                return redirect(request.META.get("HTTP_REFERER"))



# ******************* ADMIN PAGE VIEW *****************************
@login_required(login_url="website:admin_login")   
def dashboard(request):
    return render(request, 'dashboard/home.html')

# ******************* ADMIN REVIEW *****************************
@login_required(login_url="website:admin_login")   
def review(request):
    messages_count = Message.objects.all().count()
    reviews_count = Review.objects.all().count()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form .is_valid():
            review_form .save()
            messages.success(request,' review added successfully')
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        review_form  = ReviewForm()
    context = {
            'review_form': review_form,
            'reviews_count':reviews_count,
            'messages_count':messages_count
        }
    return render(request, 'dashboard/reviews.html', context)

# ******************* ADMIN MESSAGE *****************************
@login_required(login_url="website:admin_login")   
def message(request):
    reviews_count = Review.objects.all().count()
    messages_count = Message.objects.all().count()
    messages = Message.objects.all().order_by("-id")
    context = {
        'messages': messages,
        'messages_count':messages_count,
        'reviews_count':reviews_count,
    }
    return render(request, 'dashboard/message.html', context)

# ******************* ADMIN LOGIN *****************************
def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff and user.is_superuser:
            login(request, user)
            return redirect('website:dashboard')

        else:
            messages.error(request, "Invalid Credential")
            return redirect("website:admin_login")

    return render(request, 'dashboard/login.html')

# ******************* ADMIN LOGOUT  VIEW *****************************
def log_out(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("website:admin_login")
