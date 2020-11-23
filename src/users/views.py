from django.shortcuts import render
from users.models import User
from django.http import HttpResponseRedirect

# Create your views here.
def log_in_view(request):
    context = {}
    return render(request,"login.html", context)

def registration_view(request):
    redirect_to = "/"
    if  request.method == 'POST':
        if request.POST.get("password") == request.POST.get("repeat_password"):
            user = User()
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user.password = request.POST.get("password")
            user.phone_number = request.POST.get("phone_number")
            return HttpResponseRedirect(redirect_to)
    context = {}
    return render(request,"registration.html", context)