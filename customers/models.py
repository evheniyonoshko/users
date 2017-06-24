# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.utils import timezone

from users import settings



__author__ = 'Yevhenii Onoshko'


class UserManager(auth_models.BaseUserManager):
    """
    Custom User Manager. Needed for Django auth to work with custom User model
    """
    def create_user(self, email, password, is_super=False, **kwargs):
        """
        Creates and saves User
        """
        if not email:
            raise ValueError('Users must have an email address')
        if is_super:
            user = self.model(
                email=UserManager.normalize_email(email),
            )
            user.save(using=self._db)
        else:
            user = self.model(
                name=kwargs['name'] or None,
                email=UserManager.normalize_email(email),
                phone=kwargs['phone'] or None,
                mobile_phone=kwargs['phone'] or None,
                )
            user.save(using=self._db)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """
        Creates and saves superuser
        """
        user = self.create_user(email=email, password=password, is_super=True )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(auth_models.PermissionsMixin, auth_models.AbstractBaseUser):
    """
    Custom User Model. Use email as username.
    Needed to override default Django User which use username as username :)

    """
    registered = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=128, unique=True)
    name = models.CharField('Name', max_length=128)
    first_name = models.CharField('First Name', max_length=128, blank=True, null=True)
    last_name = models.CharField('Last Name', max_length=128, blank=True, null=True)
    phone = models.CharField('Phone', max_length=128, blank=True, null=True)
    mobile_phone = models.CharField('Mobile Phone', max_length=128, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.get_full_name()


    def __str__(self):
        return self.get_full_name()


    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(User, self).save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields
        )

    def has_module_perms(self, app_label):
        return True


class Courses(models.Model):
    name = models.CharField('Name', max_length=128)
    code = models.CharField('Code', max_length=128)
