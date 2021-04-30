from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("search/", include("haystack.urls")),
    path("api/", include("searches.urls")),
]
