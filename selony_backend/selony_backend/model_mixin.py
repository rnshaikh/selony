from django.db import models

from user_management.models import User


class CreateUserInfo(models.Model):

    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   blank=True, null=True,
                                   related_name='created_%(class)ss')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True


class UpdateUserInfo(models.Model):

    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   blank=True, null=True,
                                   related_name='updated_%(class)ss')
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
