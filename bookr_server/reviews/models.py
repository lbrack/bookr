""" For information on how this model was created, check
    https://subscription.packtpub.com/book/web-development/9781803230603/2/ch02lvl1sec20/creating-django-models-and-migrations

"""
from django.db import models

# Create your models here.


class Publisher(models.Model):
    """A Company that publishes books."""

    name = models.CharField(max_length=50, help_text="Name of the publisher")
    website = models.URLField(help_text="Publisher's website")
    email = models.EmailField("Publisher's email address")
