from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.password_validation import validate_password


class UserManager(BaseUserManager):

    def create_user(self, email, password):

        if not email:
            raise ValueError("User must have email address.")
        validate_password(password)

        user = self.model(email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)
    password = models.CharField(max_length=256)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('password',)

    objects = UserManager()

    def __str__(self):
        return self.email
