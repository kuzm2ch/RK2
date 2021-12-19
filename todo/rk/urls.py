from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/', include('api.urls')),
    path('computer/<int:id>/', views.GetComputer, name='computer_url')
]