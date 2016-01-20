from staff.models import IthacashStaff
from django.contrib.auth.hashers import check_password


class IthacashStaffBackend(object):

    def authenticate(self, email=None, password=None):
        user = IthacashStaff._default_manager.get_by_natural_key(email)

        if check_password(password, user.password):
            return user

    def get_user(self, id):
        try:
            return IthacashStaff.objects.get(pk=id)
            print email
        except IthacashStaff.DoesNotExist:
            return None
