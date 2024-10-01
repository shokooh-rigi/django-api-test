import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from estimate.models import Estimate, EstimateEquipment
from .factories import UserFactory, EquipmentFactory, EstimateFactory


@pytest.mark.django_db
def test_create_estimate():
    """
    Test for creating a new estimate via API.
    """
    client = APIClient()

    # GIVEN: A user and equipment exist for creating an estimate.
    user = UserFactory()  # Create a user using the factory
    client.force_authenticate(user=user)  # Authenticate the user
    equipment = EquipmentFactory()  # Create equipment using the factory

    # Data for creating a new estimate
    data = {
        "note": "New Estimate",
        "created_by": user.id,
        "equipments": [
            {
                "equipment": equipment.id,
                "quantity": 10,
                "price_override": 120.50
            }
        ]
    }

    # WHEN: A request is made to create a new estimate.
    url = reverse('create-estimate')
    response = client.post(url, data, format='json')

    # THEN: The estimate should be successfully created along with its related equipments.
    assert response.status_code == 201
    assert Estimate.objects.count() == 1
    assert EstimateEquipment.objects.count() == 1
    assert response.data['note'] == "New Estimate"


@pytest.mark.django_db
def test_update_estimate():
    """
    Test for updating an existing estimate via API.
    """
    client = APIClient()

    # GIVEN: An existing estimate and equipment exist for updating.
    estimate = EstimateFactory()  # Create an estimate using the factory
    user = estimate.created_by  # Get the user who created the estimate
    client.force_authenticate(user=user)  # Authenticate the user

    # Data for updating the estimate
    data = {
        "note": "Updated Estimate",
        "created_by": user.id,
        "archive": True,
        "equipments": []  # Optionally clear the equipments
    }

    # WHEN: A request is made to update the estimate.
    url = reverse('estimate-detail', args=[estimate.id])
    response = client.put(url, data, format='json')

    # THEN: The estimate should be updated successfully with the new data.
    assert response.status_code == 200
    estimate.refresh_from_db()
    assert estimate.note == "Updated Estimate"
    assert estimate.archive is True


@pytest.mark.django_db
def test_delete_estimate():
    """
    Test for deleting an existing estimate via API.
    """
    client = APIClient()

    # GIVEN: An existing estimate to delete.
    estimate = EstimateFactory()  # Create an estimate using the factory
    user = estimate.created_by  # Get the user who created the estimate
    client.force_authenticate(user=user)  # Authenticate the user

    # WHEN: A request is made to delete the estimate.
    url = reverse('estimate-detail', args=[estimate.id])
    response = client.delete(url)

    # THEN: The estimate and its related equipments should be successfully deleted.
    assert response.status_code == 204
    assert Estimate.objects.count() == 0
    assert EstimateEquipment.objects.count() == 0  # Ensure related equipment is also deleted
