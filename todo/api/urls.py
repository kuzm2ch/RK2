from django.urls import path, include
from .views_api import ComputerListAPIView, ProgramListAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'computers', ComputerListAPIView)
router.register(r'programs', ProgramListAPIView)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]