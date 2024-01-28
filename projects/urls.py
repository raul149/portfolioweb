from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.blog_page, name='blog_page'),  # Adjust the path and view as needed
]