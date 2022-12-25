from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from utils.util import get_random_string


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name_plural = _('Users')
        verbose_name = _('User')
        db_table = "user"
        ordering = ["pk"]

    username = models.CharField(_('username'), max_length=255, blank=True, null=True, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone")
    avatar = models.FileField(upload_to="avatars", max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=100, blank=True, null=True, unique=True)

    date_joined = models.DateTimeField(default=timezone.now, blank=True, null=True)
    is_deleted = models.BooleanField(default=False, blank=True, null=True)
    deleted_by = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE,
                                   related_name="user_deleted_by")
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('User', blank=True, null=True, on_delete=models.CASCADE,
                                   related_name="user_created_by")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def save(self, *args, **kwargs):
        is_new = self.id is None
        self.username = self.email
        if is_new:
            """
            Be sure a unique string
            """
            secret = get_random_string(50)
            while User.objects.filter(secret=secret).exists():
                secret = get_random_string(50)
            self.secret = secret

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
