from staff.models import IthacashStaff
from django.contrib.auth.hashers import check_password
from django.core.exceptions import PermissionDenied


class IthacashStaffBackend(object):

    def authenticate(self, username=None, password=None):
        try:
            user = IthacashStaff._default_manager.get_by_natural_key(username)

            if check_password(password, user.password) and user.confirmed:
                return user

        except:
            raise PermissionDenied

    def get_user(self, id):
        try:
            return IthacashStaff.objects.get(pk=id)
        except IthacashStaff.DoesNotExist:
            return None
