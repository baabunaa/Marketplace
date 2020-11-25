from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home_view, sports_view, music_and_art_view, electronics_view, home_technics_view

urlpatterns = [
    path('', home_view, name='home'),
    path('sports/', sports_view, name='sport'),
    path('music/', music_and_art_view, name='music and art'),
    path('electronics/', electronics_view, name='electronics'),
    path('technics/', home_technics_view, name='home technics'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
