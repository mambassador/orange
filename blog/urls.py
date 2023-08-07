from django.urls import path
from blog import views
from blog.views import UserUpdateView, ContactView

app_name = "blog"

urlpatterns = [
    path("profile/update/", UserUpdateView.as_view(), name="user_update"),
    path("user/<int:pk>", views.UserDetailView.as_view(), name="user_detail"),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("posts/", views.PostListView.as_view(), name="posts"),
    path("my_posts/<int:pk>", views.UserPostListView.as_view(), name="my_posts"),
    path("create/", views.PostCreateView.as_view(), name="create"),
    path("update/<int:pk>", views.PostUpdateView.as_view(), name="update"),
    path("contact/", ContactView.as_view(), name="contact"),
]
