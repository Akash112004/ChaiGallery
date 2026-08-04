from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='home'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('categories/', views.categories, name='categories'),
    path('update/<int:tea_id>/', views.edit_tea, name='edit_tea'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile, name='profile'),
    
]
