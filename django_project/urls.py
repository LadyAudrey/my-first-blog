from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include("blogs.urls")),
    #path('', include("pages.urls")), #do I need to comment this out for blogs to be visible?
]