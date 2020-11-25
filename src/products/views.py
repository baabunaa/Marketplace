from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
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
    sport_products = Post.objects.filter(category='sp')
    context = {'title': 'Sports', 'all_products': sport_products}
    return render(request, "category_products.html", context)


def music_and_art_view(request):
    ma_products = Post.objects.filter(category='ma')
    context = {'title': 'Music & Arts', 'all_products': ma_products}
    return render(request, "category_products.html", context)


def electronics_view(request):
    elec_products = Post.objects.filter(category='el')
    context = {'title': 'Electronics', 'all_products': elec_products}
    return render(request, "category_products.html", context)


def home_technics_view(request):
    home_products = Post.objects.filter(category='ht')
    context = {'title': 'Home Technichs', 'all_products': home_products}
    return render(request, "category_products.html", context)


def post_view(request):
    form = PostForm()
    context={'form':form}
    return render(request,"create_post.html",context)