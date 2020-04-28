from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

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

ImageTypes = (
    (0, 'UserProfile'),
    (1, 'BlogPost'),
    (2, 'ShopItem'),
    (3, 'SectionHeader')
)


class Fee(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.amount)


class Image(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(storage=fs)
    name = models.CharField(max_length=120)
    type = models.IntegerField(choices=ImageTypes)

    def __str__(self):
        return self.name


# Create your models here.
class Socio(AbstractUser):
    type = models.IntegerField(choices=USER_TYPES, default=3)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=150, unique=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    fee = models.OneToOneField(Fee, on_delete=models.DO_NOTHING, null=True)
    profile_img = models.ForeignKey(Image, on_delete=models.DO_NOTHING, null=True)

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

    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING, null=True)

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
        return str(self.percentage)



