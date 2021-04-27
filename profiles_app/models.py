from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser #
from django.contrib.auth.models import PermissionsMixin #overwrite django models
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    def create_user(self,email:str, password:str=None):
        """Create new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email)

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email,password):
        user=self.create_user(email,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email=models.EmailField(max_length=255, unique=True)
    name= models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects= UserProfileManager()#when the client create user in Django CLI

    USERNAME_FIELD='email' #overwrite USERNAME_FIELD by default
    #REQUIRED_FIELD=['name'] #Required when the user create a user


    def get_full_name(self):
        """Retrieve return full name user
        """
        return self.name

 
    
    def __str__(self):
        """Return string representation of user"""
        return self.email










