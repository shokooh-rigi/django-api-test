from django.db import models
from management.models import Equipment
from test.base_model import BaseModel
from user.models import User


def estimate_number_generator(estimate_id):
    """
    Generates a unique estimate number based on the creation date
    and user ID.

    Args:
        estimate_id (int): ID of the estimate object.

    Returns:
        str: The generated estimate number.
    """
    estimate = Estimate.objects.get(id=estimate_id)
    estimator_long_id = estimate.created_by.id + 100
    estimate_date_created = str(estimate.created_on).replace('-', '')[2:8]
    return estimate_date_created + str(estimator_long_id) + str(estimate.id).zfill(3)


class Estimate(BaseModel):
    """
    Model representing an estimate created by a user with notes and status.

    Attributes:
        note (str): Optional field for adding notes about the estimate.
        created_by (User): Foreign key relation to the user who created the estimate.
        archive (bool): Boolean flag to archive the estimate.
    """
    note = models.TextField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    archive = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        """
        String representation of the estimate, including generated estimate number.

        Returns:
            str: Generated estimate number or placeholder text for unsaved instances.
        """
        if self.id:
            return estimate_number_generator(self.id)
        return "New Estimate (unsaved)"


class EstimateEquipment(BaseModel):
    """
    Model representing the relationship between an estimate and equipment.

    Attributes:
        estimate (Estimate): Foreign key relation to the estimate.
        equipment (Equipment): Foreign key relation to the equipment.
        quantity (float): Quantity of equipment used in the estimate.
        price_override (decimal): Optional field for overriding the equipment price.
    """
    estimate = models.ForeignKey(Estimate, on_delete=models.CASCADE, blank=False, null=False)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, blank=False)
    quantity = models.FloatField(blank=False)
    price_override = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        """
        String representation of the estimate equipment relationship.

        Returns:
            str: Estimate number with equipment name.
        """
        return estimate_number_generator(self.estimate.id) + " " + self.equipment.name
