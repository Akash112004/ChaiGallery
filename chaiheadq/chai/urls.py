from django.urls import path
from . import views

     
urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('gallery/', views.gallery, name='gallery'),
    path('categories/', views.categories, name='categories'),
    path('update/<int:tea_id>/', views.edit_tea, name='edit_tea'),
    path('delete/<int:tea_id>/', views.tea_delete, name='tea_delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path("logout/", views.logout_view, name="logout"),
]
    

