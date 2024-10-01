from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipmentViewSet

router = DefaultRouter()
router.register(r'equipments', EquipmentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
