from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('editprofile/<str:pk>/', views.editprofile, name='editprofile'),
    path('post/', views.post, name='post'),
    path('article/', views.article, name='article'),
    path('article/<str:pk>',views.article,name='article'),
    path('editarticle/<str:pk>',views.editarticle,name='editarticle'),
    path('deletearticle/<str:pk>',views.deletearticle,name='deletearticle'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    # path('edit-article/',views.home,name='edit-article'),
    # path('delete-article/',views.home,name='delete-article'),
]
