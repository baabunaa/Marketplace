from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    context = {}
    return render(request, "home.html", context)

def log_in_view(request):
    context = {}
    return render(request,"login.html", context)