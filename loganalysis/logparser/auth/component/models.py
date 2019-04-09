from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager

from ..constants import ROLES

class User_manager(BaseUserManager):
    def create_user(self, username, email, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, gender="0", nickname=None)
        user.set_password(password)
        user.role = ROLES.ROLE_USER
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, gender, password):
        user = self.create_user(username=username, email=email, gender=gender, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.role = ROLES.ROLE_ADMIN
        user.save()
        return user


class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(max_length=100)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    nickname = models.CharField(max_length=32, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=20)

    REQUIRED_FIELDS = ["email", "gender", "role"]
    USERNAME_FIELD = "username"
    objects = User_manager()

    def __str__(self):
        return self.username + ' ' + self.role

