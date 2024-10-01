from management.models import Equipment
from factory import Faker
from factory.django import DjangoModelFactory


class EquipmentFactory(DjangoModelFactory):
    class Meta:
        model = Equipment

    name = Faker('word')
    price = Faker('random_number', digits=5)
    flag = True
