from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helper class for django to work with our model"""

    def create_user(self, email, name, password=None):
        """Creates a new user profile"""

        # check if an email is provided
        if not email:
            raise ValueError('Users must have an email address.')
        
        # normalize email address
        email = self.normalize_email(email)

        # create user profile model object
        user = self.model(email=email, name=name)
        user.set_password(password)

        # save the user in the database
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password=None):
        """Creates a new superuser profile"""

        # create a new user entry model
        user = self.create_user(email, name, password)

         # assign user as a superuser
        user.is_superuser = True
        user.is_staff = True


        # save the user in the database
        user.save(using=self._db)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system"""

    # define model fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # class helps manage user profiles 
    objects = UserProfileManager()

    # field that will be used as the username for the user to login
    USERNAME_FIELD = 'email'

    # list of fields that are required
    REQUIRED_FIELDS = ['name']

    # helper functions
    def get_full_name(self):
        """Used to get a user's full name"""

        return self.name

    def get_short_name(self):
        """Used to get a user's short name"""

        return self.name


    def __str__(self):
        """Converts object to a String"""

        return self.email