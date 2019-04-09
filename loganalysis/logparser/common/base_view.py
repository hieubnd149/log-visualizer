from rest_framework import permissions, generics
from rest_framework_role_filters.role_filters import RoleFilterGroup
from rest_framework_role_filters.viewsets import RoleFilterModelViewSet

from ..auth.component.role_filters import UserRoleFilter, AdminRoleFilter

class BaseView(RoleFilterModelViewSet):
    def __init__(self):
        role_filter_group = RoleFilterGroup(role_filters=self.get_filter_group())

    
    def get_filter_group(self):
        return []

    
    def get_role_id(self, request):
        print(request.user.role)
        return request.user.role

    
    def getUserRole():
        return UserRoleFilter()

    
    def getAdminRole():
        return AdminRoleFilter()