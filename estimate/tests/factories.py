# estimate/factories.py
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory
from estimate.models import Estimate, EstimateEquipment
from management.tests.factories import EquipmentFactory
from user.tests.factories import UserFactory


class EstimateFactory(DjangoModelFactory):
    class Meta:
        model = Estimate

    note = Faker('text', max_nb_chars=255)
    created_by = SubFactory(UserFactory)


class EstimateEquipmentFactory(DjangoModelFactory):
    class Meta:
        model = EstimateEquipment

    estimate = SubFactory(EstimateFactory)
    equipment = SubFactory(EquipmentFactory)
    quantity = Faker('random_int', min=1, max=100)
    price_override = Faker(
        'pydecimal',
        positive=True,
        min_value=0.01,
        max_value=10000,
        right_digits=2,
    )
