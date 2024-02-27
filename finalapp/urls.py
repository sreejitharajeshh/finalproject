from . import views
from django.urls import path

app_name = 'finalapp'

urlpatterns = [
    path('', views.register, name='register'),
    path('login', views.login, name='login'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('add', views.add, name='add'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
    path('review', views.review, name='review'),
    path('category/<str:genre>/', views.category, name='category'),
    path('search', views.search, name='search'),

]
