from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='post_list'),
    path('blog/<slug:slug>', views.post, name='post_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]
