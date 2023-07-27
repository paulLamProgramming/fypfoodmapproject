from django.urls import path
from . import views
app_name = 'post'
urlpatterns = [
    path('post_list/', views.post_list, name="list"),
    path('post_detail/<int:pk>/', views.post_detail, name="detail"),
    path('post_create/', views.post_create, name="create"),
    ]
