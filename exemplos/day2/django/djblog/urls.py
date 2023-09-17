from django.contrib import admin
from django.urls import path, include
from blog.views import new_post, PostList, PostDetail
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("new/", new_post, name="new_post"),
    path("", PostList.as_view(), name="index"),
    path("<slug:slug>/", PostDetail.as_view(), name="detail"),
]
