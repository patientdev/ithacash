import factory
from accounts.models import IthacashUser, IthacashAccount


class IthacashUserFactory(factory.DjangoModelFactory):

    class Meta:
        model = IthacashUser


class IthacashAccountFactory(factory.DjangoModelFactory):

    class Meta:
        model = IthacashAccount

    owner = factory.SubFactory(IthacashUserFactory)
    account_type = "Standard Business"

    entity_name = "Nobody's Busienss"
    billing_frequency = "Monthly"

    address_1 = "1 Nowhere lane"
    