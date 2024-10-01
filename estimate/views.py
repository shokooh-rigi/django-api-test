from rest_framework import generics
from .models import Estimate
from .serializers import EstimateSerializer


class EstimateCreateView(generics.CreateAPIView):
    """
    API view for creating a new Estimate.

    This view handles POST requests to create a new estimate along with its related equipments.
    """
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer


class EstimateDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, or deleting an Estimate.

    This view supports GET, PUT, PATCH, and DELETE methods for an estimate object.
    """
    queryset = Estimate.objects.all()
    serializer_class = EstimateSerializer
