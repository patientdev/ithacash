import factory
from staff.models import IthacashStaff


class IthacashStaffFactory(factory.DjangoModelFactory):

    class Meta:
        model = IthacashStaff
        django_get_or_create = ('email',)

    email = 'faker@ithacash.com'
    is_staff = True
