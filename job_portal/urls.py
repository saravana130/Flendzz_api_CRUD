from django.urls import path
from rest_framework import routers

from .views import JobsViewSet, JobApply, JobViewSet

# router = routers.DefaultRouter()
# router.register(r'', JobsViewSet)
# router.register(r'JobApplicantViewSet', JobApplicantViewSet)

urlpatterns = [
    path('job/', JobsViewSet.as_view()),
    path('job/<int:id>/', JobViewSet.as_view()),
    path('job/<int:id>/apply', JobApply.as_view()),
]