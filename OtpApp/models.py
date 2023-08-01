from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
# Create your models here.

# we are extending a AbstractUser which means we are happy with the by default fields we only want to remove username and wants
# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    is_phone_verified = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, null=True, blank=True)
    email_verification_token = models.CharField(max_length=200, null=True, blank=True)
    forget_verification_token = models.CharField(max_length=200, null=True, blank=True)
    # don't write is_staff it will added automatically

    objects = UserManager()

    # use email fields to login
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []        # there's no required fields
     
    def __str__(self):
        return self.email
