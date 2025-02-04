from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, surname, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must enter an email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, surname=surname)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, surname, password):
        """Create and return a superuser"""
        user = self.create_user(email, name, surname, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "surname"]

    def get_full_name(self):
        """Retrieve full name of user"""
        return f"{self.name} {self.surname}"

    def __str__(self):
        """Return string representation of our user"""
        return self.email
