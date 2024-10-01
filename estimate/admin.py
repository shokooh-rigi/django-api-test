from django.contrib import admin
from .models import Estimate, EstimateEquipment


@admin.register(Estimate)
class EstimateAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for Estimate model.

    This class defines how the Estimate model is displayed and
    searched in the admin interface.
    """
    list_display = ['id', 'created_by', 'archive', 'created_at']
    search_fields = ['created_by__username', 'archive']


@admin.register(EstimateEquipment)
class EstimateEquipmentAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for EstimateEquipment model.

    This class defines how the EstimateEquipment model is displayed
    and searched in the admin interface.
    """
    list_display = ['id', 'estimate', 'equipment', 'quantity', 'price_override']
    search_fields = ['estimate__id', 'equipment__name']
