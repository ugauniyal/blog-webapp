from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", PostListView.as_view(), name="Blog-Home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="Post-Detail"),
    path("post/new", PostCreateView.as_view(), name="Post-Create"),
    path("post/<int:pk>/update", PostUpdateView.as_view(), name="Post-Update"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="Post-Delete"),
    path("about/", views.about, name="Blog-About"),
    path("contact/", views.contact, name="Contact Us"),
]

urlpatterns += staticfiles_urlpatterns()