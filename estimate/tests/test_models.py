# estimate/tests/test_models.py
from django.test import TestCase
from estimate.models import Estimate, EstimateEquipment
from estimate.tests.factories import EstimateFactory, EstimateEquipmentFactory
from management.tests.factories import EquipmentFactory
from user.tests.factories import UserFactory


class EstimateTestCase(TestCase):
    def setUp(self):
        # GIVEN: A user and an estimate are created
        self.user = UserFactory()
        self.estimate = EstimateFactory(created_by=self.user)

    def test_create_estimate(self):
        # WHEN: A new estimate is created
        new_estimate = EstimateFactory(created_by=self.user, note="Test Note")

        # THEN: The estimate should be created correctly
        self.assertEqual(new_estimate.note, "Test Note")
        self.assertEqual(new_estimate.created_by, self.user)

    def test_update_estimate(self):
        # WHEN: The note of the existing estimate is updated
        self.estimate.note = "Updated Note"
        self.estimate.save()

        # THEN: The estimate's note should reflect the update
        self.assertEqual(self.estimate.note, "Updated Note")

    def test_delete_estimate(self):
        # GIVEN: A new estimate is created
        estimate_to_delete = EstimateFactory(created_by=self.user)

        # WHEN: The estimate is deleted
        estimate_id = estimate_to_delete.id
        estimate_to_delete.delete()

        # THEN: The estimate should no longer exist
        with self.assertRaises(Estimate.DoesNotExist):
            Estimate.objects.get(id=estimate_id)


class EstimateEquipmentTestCase(TestCase):
    def setUp(self):
        # GIVEN: An estimate and an equipment are created
        self.user = UserFactory()
        self.estimate = EstimateFactory(created_by=self.user)
        self.equipment = EquipmentFactory()  # Assuming you have this factory set up

    def test_create_estimate_equipment(self):
        # WHEN: A new estimate equipment is created
        estimate_equipment = EstimateEquipmentFactory(estimate=self.estimate, equipment=self.equipment)

        # THEN: The estimate equipment should be created correctly
        self.assertEqual(estimate_equipment.estimate, self.estimate)
        self.assertEqual(estimate_equipment.equipment, self.equipment)

    def test_update_estimate_equipment(self):
        # GIVEN: An estimate equipment is created
        estimate_equipment = EstimateEquipmentFactory(estimate=self.estimate, equipment=self.equipment)

        # WHEN: The quantity is updated
        estimate_equipment.quantity = 10
        estimate_equipment.save()

        # THEN: The quantity should reflect the update
        self.assertEqual(estimate_equipment.quantity, 10)

    def test_delete_estimate_equipment(self):
        # GIVEN: An estimate equipment is created
        estimate_equipment = EstimateEquipmentFactory(estimate=self.estimate, equipment=self.equipment)

        # WHEN: The estimate equipment is deleted
        estimate_id = estimate_equipment.id
        estimate_equipment.delete()

        # THEN: The estimate equipment should no longer exist
        with self.assertRaises(EstimateEquipment.DoesNotExist):
            EstimateEquipment.objects.get(id=estimate_id)
