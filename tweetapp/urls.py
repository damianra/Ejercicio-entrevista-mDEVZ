from django.urls import path, include
from rest_framework import routers
from .model.models import SearchHistory
from .views import views

router = routers.DefaultRouter()
router.register(r'search', views.SearchAPIView, basename='search')
router.register(r'history', views.SearchHistoryAPIView, basename='history')

urlpatterns = [
    path('', views.index, name='index'),
    path('hist/', views.history, name='hist'),
    path('v1/', include(router.urls)),
]
