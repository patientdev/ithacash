import factory
from signup.models import SignUp


class SignupFactory(factory.DjangoModelFactory):

    class Meta:
        model = SignUp

    account_type = "Individual"
    name_business = "Llama Zone"
    name_contact = "Llama John"
    name_login = "llamaman"
    email = "llamaman@llamazone.com"
    address_1 = "1 llama drive"
    phone_landline = "4445559090"
    txt2pay = False
    txt2pay_phone = False