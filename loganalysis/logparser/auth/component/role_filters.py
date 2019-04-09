from rest_framework_role_filters.role_filters import RoleFilter

from ..constants import ROLES

class AdminRoleFilter(RoleFilter):
    role_id = ROLES.ROLE_ADMIN


class UserRoleFilter(RoleFilter):
    role_id = ROLES.ROLE_USER

