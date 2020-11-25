from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from users.models import UserAccount
from .forms import PostForm
# Create your views here.
def home_view(request):
    sport_products = Post.objects.filter(category='sp')[:4]
    ma_products = Post.objects.filter(category='ma')[:4]
    elec_products = Post.objects.filter(category='el')[:4]
    home_products = Post.objects.filter(category='ht')[:4]
    last_products = Post.objects.all()[:3]
    context = {
            'ma_products': ma_products,
            'sport_products': sport_products,
            'elec_products': elec_products,
            'home_products': home_products,
            'last_products': last_products
    }
    return render(request, "home.html", context)


def sports_view(request):
    last_three = Post.objects.filter(category='sp')[:3]
    sport_products = Post.objects.filter(category='sp')[3:]
    context = {'title': 'Sports', 'all_products': sport_products, 'last_three': last_three}
    return render(request, "category_products.html", context)


def music_and_art_view(request):
    last_three = Post.objects.filter(category='ma')[:3]
    ma_products = Post.objects.filter(category='ma')[3:]
    context = {'title': 'Music & Arts', 'all_products': ma_products, 'last_three': last_three}
    return render(request, "category_products.html", context)


def electronics_view(request):
    last_three = Post.objects.filter(category='el')[:3]
    elec_products = Post.objects.filter(category='el')[3:]
    context = {'title': 'Electronics', 'all_products': elec_products, 'last_three': last_three}
    return render(request, "category_products.html", context)


def home_technics_view(request):
    last_three = Post.objects.filter(category='ht')[:3]
    home_products = Post.objects.filter(category='ht')[3:]
    context = {'title': 'Home Technichs', 'all_products': home_products, 'last_three': last_three}
    return render(request, "category_products.html", context)


def post_view(request):
    redirect_to = "/"
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        name = request.POST.get("name")
        price = request.POST.get("price")
        category = request.POST.get("category")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        user = UserAccount.objects.get(user_id=request.user.id)
        if  form.is_valid():
            post = Post()
            post.name = name
            post.price = price
            post.category = category
            post.description = description
            post.picture = image
            post.user = user
            post.save()
            return HttpResponseRedirect(redirect_to)
    form = PostForm()
    context={'form':form}
    return render(request,"create_post.html",context)
    