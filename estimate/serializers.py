from rest_framework import serializers
from .models import Estimate, EstimateEquipment


class EstimateEquipmentSerializer(serializers.ModelSerializer):
    """
    Serializer for EstimateEquipment model.

    Serializes the EstimateEquipment model fields for API representation.
    """

    class Meta:
        model = EstimateEquipment
        fields = [
            'id',
            'equipment',
            'quantity',
            'price_override',
            'created_at',
        ]


class EstimateSerializer(serializers.ModelSerializer):
    """
    Serializer for Estimate model with related EstimateEquipment.

    Serializes Estimate model and its related equipments.
    """
    equipments = EstimateEquipmentSerializer(many=True, required=False)
    equipments_list = EstimateEquipmentSerializer(
        source='estimateequipment_set',
        many=True,
        required=False,
    )

    class Meta:
        model = Estimate
        fields = [
            'id',
            'note',
            'created_at',
            'created_by',
            'archive',
            'equipments',
            'equipments_list',
        ]

    def create(self, validated_data):
        """
        Custom create method to handle nested EstimateEquipment creation.

        Args:
            validated_data (dict): Data validated by the serializer.

        Returns:
            Estimate: Created Estimate instance.
        """
        equipments_data = validated_data.pop('equipments', [])
        estimate = Estimate.objects.create(**validated_data)

        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=estimate, **equipment_data)

        return estimate

    def update(self, instance, validated_data):
        """
        Custom update method to handle updating Estimate and related EstimateEquipment.

        Args:
            instance (Estimate): Existing estimate instance.
            validated_data (dict): Updated data.

        Returns:
            Estimate: Updated estimate instance.
        """
        equipments_data = validated_data.pop('equipments', [])

        # Update the Estimate object
        instance.note = validated_data.get('note', instance.note)
        instance.archive = validated_data.get('archive', instance.archive)
        instance.save()

        instance.estimateequipment_set.all().delete()
        for equipment_data in equipments_data:
            EstimateEquipment.objects.create(estimate=instance, **equipment_data)

        return instance
