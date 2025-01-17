from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid

USER_TYPES = (
    (0, 'Admin'),
    (1, 'Socio'),
    (2, 'Trabajador'),
    (3, 'Voluntario')
)

PROJECT_UNITS = (
    (0, 'hectareas'),
    (1, 'árboles'),
    (2, 'toneladas'),
    (3, 'euros')
)


class Fee(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(default=0.0)


# Create your models here.
class Socio(AbstractUser):
    type = models.IntegerField(choices=USER_TYPES, default=3)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    fee = models.OneToOneField(Fee, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        verbose_name = "Socio"

    def __str__(self):
        return self.username


class Project(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    unit = models.IntegerField(choices=PROJECT_UNITS, default=3)
    description = models.TextField()
    visible = models.BooleanField(default=True)
    got = models.IntegerField()
    goal = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyecto"

    def __str__(self):
        return self.title


class FeeDistribution(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    percentage = models.FloatField(default=0.0)

    fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = "DistribucionCuota"

    def __str__(self):
        return self.percentage
