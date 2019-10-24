from django.db import models

# Create your models here.
import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)

from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, first_name=None, last_name=None):
        if username is None:
            raise TypeError('User must have a username.')
        if email is None:
            raise TypeError('User must have an email address.')
        
        user = self.model(username=username, email=self.normalize_email(email), first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, username, email, password, first_name=None, last_name=None):
        if password is None:
            raise TypeError('Superuser must have a password.')

        user = self.create_user(username, email, password, first_name, last_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def get_full_name(self):
        if self.first_name is not None and self.last_name is not None:
            return '{} {}'.format(self.first_name, self.last_name)
        return self.get_username()

    def get_short_name(self):
        if self.first_name is not None:
            return self.first_name

    def get_username(self):
        return self.username

    def is_admin(self):
        return self.is_staff

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
