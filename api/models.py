from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Socio(AbstractUser):
    USER_TYPES = (
        (0, 'Admin'),
        (1, 'Socio'),
        (2, 'Trabajador'),
        (3, 'Voluntario')
    )
    type = models.IntegerField(choices=USER_TYPES, default=3)
    fee = models.FloatField(default=0.0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
