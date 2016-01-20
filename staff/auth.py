from staff.models import IthacashStaff
from django.contrib.auth.hashers import check_password
from django.core.exceptions import PermissionDenied


class IthacashStaffBackend(object):

    def authenticate(self, email=None, password=None):
        user = IthacashStaff._default_manager.get_by_natural_key(email)

        if check_password(password, user.password) and user.confirmed:
            return user

        else:
            raise PermissionDenied

    def get_user(self, id):
        try:
            return IthacashStaff.objects.get(pk=id)
            print email
        except IthacashStaff.DoesNotExist:
            return None
