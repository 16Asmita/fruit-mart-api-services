from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    username = models.CharField(max_length=50, unique=True, blank=False, null=False)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=False, null=False)
    last_login = models.DateTimeField(blank=True, null=True)
    
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'user_account'


