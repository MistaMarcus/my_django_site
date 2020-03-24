from django.urls import path
from . import views


urlpatterns = [
    #if you go to local host it will take you here
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]
