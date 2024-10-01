from django.db import models


class BaseModel(models.Model):
    """
    Base model to provide created_at and updated_at fields for other models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
