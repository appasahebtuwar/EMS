from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Users(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    email = models.EmailField(unique=True)
    address = models.TextField()
    dob = models.DateField()
    company = models.CharField(max_length=55)
    mobile = PhoneNumberField(
        help_text='Must include international prefix - e.g. +1 555 555 55555', )
    city = models.CharField(max_length=55, null=True, blank=True)
    is_manager = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    employee_id = models.CharField(max_length=20)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    objects = UserManager()
