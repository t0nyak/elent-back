from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

USER_TYPES = (
    (0, 'Admin'),
    (1, 'Socio'),
    (2, 'Trabajador'),
    (3, 'Voluntario')
)

# Create your models here.
# class Socio(AbstractUser):
#     type = models.IntegerField(choices=USER_TYPES, default=3)
#     fee = models.FloatField(default=0.0)
#     email = models.EmailField(_('email address'), unique=True)
#     username = models.CharField(max_length=150, unique=False, blank=True)
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = "Socio"
#
#     def __str__(self):
#         return self.username
