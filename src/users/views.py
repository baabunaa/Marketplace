from django.shortcuts import render
from users.models import UserAccount
from django.http import HttpResponseRedirect
from users.forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def log_in_view(request):
    redirect_to = "/"
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(redirect_to)
    form = LoginForm()
    context = {'form': form}
    return render(request,"login.html", context)

def registration_view(request):
    redirect_to = "/"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        if  password == request.POST.get("repeat_password") and form.is_valid():
            print("valid")
            acc = UserAccount()
            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)
            acc.user = user
            acc.phone_number = request.POST.get("phone_number")
            acc.picture = request.POST.get("picture")
            acc.save()
            return HttpResponseRedirect(redirect_to)
    form = RegistrationForm()
    print("inValid")

    context = {'form': form}
    return render(request,"registration.html", context)