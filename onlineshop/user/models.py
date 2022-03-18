from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None,  **extra_fields):
        """create and save users"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """create and save superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.is_verified = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custome user model that support email insted of username"""
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    email = models.EmailField(max_length=255, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    is_verified = models.BooleanField(default=False)

    google_id = models.CharField(max_length=255, null=True, blank=True)
    facebook_id = models.CharField(max_length=255, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def full_name(self):
        full_name = None

        if self.first_name or self.last_name:
            full_name = self.first_name + " " + self.last_name
        else:
            full_name = self.email
        return full_name

    class Meta:
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email
