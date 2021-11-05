from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db.models.fields.related import RECURSIVE_RELATIONSHIP_CONSTANT

# Create your models here.

class UserAccountManager(BaseUserManager):
    # basic model
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    # creating firm account 
    def create_firm(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        
        user.is_firm = True
        user.save

        return user

    # creating lawyer account
    def create_lawyer(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        
        user.is_lawyer = True
        user.save

        return user
    
    # creating client account
    def create_client(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields )
        
        user.is_client = True
        user.save

        return user
    # creating superuser account
    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        
        user.is_superuser = True
        user.is_staff = True
        user.save

        return user

class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    
    # flags
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    is_firm = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name

    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email