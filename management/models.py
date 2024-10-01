from django.db import models

from test.base_model import BaseModel


class Equipment(BaseModel):
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    flag = models.BooleanField(default=True, help_text="Whether its active or not")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
