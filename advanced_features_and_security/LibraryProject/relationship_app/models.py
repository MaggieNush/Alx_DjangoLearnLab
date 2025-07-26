from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class CustomUser(AbstractUser):
    date_of_birth = models.DateField
    profile_photo = models.ImageField

class CustomManagerModel(BaseUserManager):
    def create_user(self, date_of_birth, profile_photo, **extra_fields):
        """
        create and save users with the given DOB and profile photo
        """
        if not date_of_birth:
            raise ValueError("The date of birth must be set")
        date_of_birth = self.date_of_birth(date_of_birth)
        user = self.model(date_of_birth=date_of_birth, **extra_fields)
        user.set_profile_photo(profile_photo)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, date_of_birth, profile_photo, **extra_fields):
        """
        create and save users with the given DOB and profile photo
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is staff=True.")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(date_of_birth, profile_photo, **extra_fields)