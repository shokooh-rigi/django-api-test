from django.test import TestCase

from .factories import EquipmentFactory
from ..models import Equipment


class EquipmentTestCase(TestCase):
    def test_equipment_creation(self):
        equipment = EquipmentFactory.create()
        self.assertTrue(isinstance(equipment, Equipment))
        self.assertEqual(Equipment.objects.count(), 1)
