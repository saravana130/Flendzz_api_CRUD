from django.contrib import admin
from django.urls import path, include
from job_portal.urls import urlpatterns as joburl

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(joburl))
]
