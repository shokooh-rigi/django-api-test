from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.tests.factories import UserFactory
from .factories import EquipmentFactory
from ..models import Equipment


class EquipmentAPITest(APITestCase):

    def setUp(self):
        self.user = UserFactory(is_staff=True)
        self.client.force_authenticate(user=self.user)  # Authenticate the test user
        self.url = reverse('equipment-list')  # URL for the equipment list

    def test_create_equipment(self):
        # Given: Necessary data to create a new equipment
        data = {
            'name': 'New Equipment',
            'price': '150.00',
            'flag': True
        }

        # When: Sending POST request to the API
        response = self.client.post(self.url, data, format='json')

        # Then: Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipment.objects.count(), 1)  # One new equipment created
        self.assertEqual(Equipment.objects.first().name, 'New Equipment')  # Check the data

    def test_list_equipment(self):
        # Given: Create equipment using the factory
        EquipmentFactory.create_batch(3)  # Create 3 equipment

        # When: Sending GET request to the API to retrieve the list of equipment
        response = self.client.get(self.url)

        # Then: Check that the response is successful and 3 equipment are returned
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_equipment(self):
        # Given: Create an equipment using the factory
        equipment = EquipmentFactory.create()

        # When: Sending GET request to retrieve a specific equipment
        url = reverse('equipment-detail', args=[equipment.id])  # URL for a specific equipment
        response = self.client.get(url)

        # Then: Check the response and the equipment data
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], equipment.name)

    def test_update_equipment(self):
        # Given: Create an equipment using the factory
        equipment = EquipmentFactory.create()

        # When: Sending PUT request to update the equipment
        url = reverse('equipment-detail', args=[equipment.id])
        updated_data = {
            'name': 'Updated Equipment',
            'price': '200.00',
            'flag': False
        }
        response = self.client.put(url, updated_data, format='json')

        # Then: Check that the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        equipment.refresh_from_db()  # Refresh from the database to get the latest data
        self.assertEqual(equipment.name, 'Updated Equipment')  # Check the updated data

    def test_delete_equipment(self):
        # Given: Create an equipment using the factory
        equipment = EquipmentFactory.create()

        # When: Sending DELETE request to delete the equipment
        url = reverse('equipment-detail', args=[equipment.id])
        response = self.client.delete(url)

        # Then: Check that the response is successful and the equipment is deleted
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Equipment.objects.count(), 0)  # Ensure no equipment remains

    def test_create_equipment_non_admin(self):
        # Given: Create a regular user (non-admin)
        non_admin_user = UserFactory(is_staff=False)
        self.client.force_authenticate(user=non_admin_user)

        # When: Sending POST request to create equipment
        data = {
            'name': 'New Equipment',
            'price': '150.00',
            'flag': True
        }
        response = self.client.post(self.url, data, format='json')

        # Then: Check that the response is forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)