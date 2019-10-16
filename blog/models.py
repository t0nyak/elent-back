from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Autores"
        verbose_name = "Autor"

    def __str__(self):
        return self.name


class Category(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name_plural = "Categorías"
        verbose_name = "Categoría"

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS = (
        (0, "Draft"),
        (1, "Published")
    )

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)

    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
