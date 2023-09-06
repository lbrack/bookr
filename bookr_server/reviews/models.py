""" For information on how this model was created, check
    https://subscription.packtpub.com/book/web-development/9781803230603/2/ch02lvl1sec20/creating-django-models-and-migrations

    For doc: https://bookr.readthedocs.io/en/latest/apps/global/models.html
"""
from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    """A Company that publishes books."""

    name = models.CharField(max_length=50, help_text="Name of the publisher")
    website = models.URLField(help_text="Publisher's website")
    email = models.EmailField("Publisher's email address")

    def __str__(self):
        return self.name


class Book(models.Model):
    """A published book."""

    title = models.CharField(max_length=70, help_text="Title of the book.")
    publication_date = models.DateField(verbose_name="Date the book was published.")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book.")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField("Contributor", through="BookContributor")

    def __str__(self):
        return self.title


class Contributor(models.Model):
    """A contributor to a Book, e.g. author, editor,
    co-author."""

    first_names = models.CharField(
        max_length=50, help_text="Contributor's first name or names."
    )
    last_names = models.CharField(
        max_length=50, help_text="Contributor's last name or names."
    )
    email = models.EmailField(help_text="Contact email for the contributor.")

    def __str__(self):
        return f"{self.first_names} {self.last_names}"


class BookContributor(models.Model):
    """This is a Junction Table for a many to many relationship
    between one or more books and one or more contributors.

    This table does not need to be explicitly created (in this
    case we want to add the contributor type in the relationship).

    """

    class ContributionRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(
        verbose_name="Role this contributor had in the book.",
        choices=ContributionRole.choices,
        max_length=20,
    )


class Review(models.Model):
    content = models.TextField(help_text="Review text.")
    rating = models.IntegerField(help_text="Rating the reviewer has given.")
    date_created = models.DateTimeField(
        auto_now_add=True, help_text="Date and time the review was created."
    )
    date_edited = models.DateTimeField(
        null=True, help_text="Date and time the review was last edited."
    )
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, help_text="Book that this review is for."
    )
