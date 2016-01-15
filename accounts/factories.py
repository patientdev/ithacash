import factory
from accounts.models import IthacashUser, IthacashAccount, Email
from django.utils.timezone import now


class IthacashUserFactory(factory.DjangoModelFactory):

    class Meta:
        model = IthacashUser
        django_get_or_create = ('username',)

    username = "faker"
    full_name = "Fakey McGee"
    created = now()


class EmailFactory(factory.DjangoModelFactory):

    class Meta:
        model = Email

    address = "fakes@faker.co"
    owner = factory.SubFactory(IthacashUserFactory)
    created = now()
    confirmed = now()
    most_recent_confirmation_key = "91358ec2820b417a9a8999da44d2432f"
    wants_to_receive_updates = True


class IthacashAccountFactory(factory.DjangoModelFactory):

    class Meta:
        model = IthacashAccount

    owner = factory.SubFactory(IthacashUserFactory)

    account_type = "Standard Business"
    entity_name = "Fake Biz, Inc."

    billing_frequency = "Monthly"

    address_1 = "PO Box 000"
    address_2 = "Apt. 2"
    city = "Trumansburg"
    state = "NY"
    zip_code = "14886"
    tin = "000000000"
    is_ssn = True
    phone_mobile = "+16072222222"
    phone_landline = "+16072222222"
    website = ""
    txt2pay = True
    txt2pay_phone = False
    electronic_signature = "X"

    created = now()
