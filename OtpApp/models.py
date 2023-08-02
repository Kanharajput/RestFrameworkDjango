from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.core.mail import send_mail
import uuid
from django.conf import settings
from .helpers import send_otp_to_mobile

# we are extending a AbstractUser which means 
# we are happy with the by default fields 
# we only want to remove username and wants
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


# this is called signal, it will automatically 
# send an email when a user succefully register 
@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    if created and not instance.is_superuser: 
        try: 
            subject = "Your email needs to be verified"
            message = f'Hi click on the link to verify https://127.0.0.1:8000/{uuid.uuid4()}/'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [instance.email]
            send_mail(subject, message, email_from, recipient_list)
            # send otp on phone to register
            send_otp_to_mobile(instance)

        except Exception as e:
            print(e)