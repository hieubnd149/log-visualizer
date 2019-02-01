from rest_framework import permissions, generics
from rest_framework_role_filters.role_filters import RoleFilterGroup
from rest_framework_role_filters.viewsets import RoleFilterModelViewSet

class BaseView(RoleFilterModelViewSet):
    def __init__(self):
        role_filter_group = self.get_filter_group()

    
    def get_filter_group(self):
        return []