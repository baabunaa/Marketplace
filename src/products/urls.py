from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sports/', views.sports_view, name='sport'),
    path('music/', views.music_and_art_view, name='music and art'),
    path('electronics/', views.electronics_view, name='electronics'),
    path('technics/', views.home_technics_view, name='home technics'),
    path('post/', views.post_view, name='post')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
