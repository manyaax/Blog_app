from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
    # ... your existing URL patterns
    path('search/', views.search_posts, name='search'),  # ✅ Add this line
]


