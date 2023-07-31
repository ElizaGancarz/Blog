from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('<int:postId>/', views.detail, name = 'detail')
]