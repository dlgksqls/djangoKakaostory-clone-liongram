from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager as DjangoUserManager

# Create your models here.

class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError("유저이름은 필수 입니다.")
        if not email:
            raise ValueError('이메일은 필수 입니다.')
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, email, password, **extra_fields)
    
    
class User(AbstractUser):
    phone = models.CharField(verbose_name='전화번호',max_length=11)
    objects = UserManager()