from rest_framework_role_filters import RoleFilter


class AdminRoleFilter(RoleFilter):
    role_id = 'admin'


class UserRoleFilter(RoleFilter):
    role_id = 'user'


