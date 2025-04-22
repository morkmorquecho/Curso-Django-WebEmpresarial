from django.urls import path
from Core import views as coreviews


urlpatterns = [
    path('', coreviews.home, name='home'),
    path('about/', coreviews.about, name='about'),
    path('store/', coreviews.store, name='store'),
    path('blog/', coreviews.blog, name='blog'),
    path('services/', coreviews.services, name='services'),
]
