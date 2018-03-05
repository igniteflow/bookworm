"""Books models."""

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django_common.auth_backends import User
from model_utils import Choices

from rest_framework.authtoken.models import Token


class Author(models.Model):
    """Author model."""

    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        """Return the string representation."""
        return self.name


class Publisher(models.Model):
    """Publisher model."""

    name = models.CharField(
        max_length=200,
    )
    description = models.TextField(
        blank=True,
    )

    def __str__(self):
        """Return the string representation."""
        return self.name


class Book(models.Model):
    """Books model."""

    GENRES = Choices(
        ('action', _('Action')),
        ('adventure', _('Adventure')),
        ('romance', _('Romance')),
        ('fiction', _('Fiction')),
        ('fantasy', _('Fantasy')),
        ('non-fiction', _('Non Fiction')),
        ('science-fiction', _('Science Fiction')),
        ('satire', _('Satire')),
        ('drama', _('Drama')),
        ('mystery', _('Mystery')),
        ('poetry', _('Poetry')),
        ('comics', _('Comics')),
        ('horror', _('Horror')),
        ('art', _('Art')),
        ('diaries', _('Diaries')),
        ('guide', _('Guide')),
        ('travel', _('Travel')),
    )

    title = models.CharField(
        max_length=200,
    )
    genre = models.CharField(
        max_length=20,
        choices=GENRES,
        default=GENRES.action,
    )
    description = models.TextField(
        blank=True,
    )
    pages = models.IntegerField(
        blank=True,
        null=True,
    )
    authors = models.ManyToManyField(
        Author,
        related_name="+",
        verbose_name=_('author'),
        blank=True,
    )
    publisher = models.ForeignKey(
        Publisher,
        related_name="+",
        verbose_name=_('publisher'),
        on_delete=models.CASCADE,
        blank=True,
    )
    published_date = models.DateField(
        blank=True,
    )

    def publish(self):
        """Publish book."""
        self.save()

    def __str__(self):
        """Return the string representation."""
        return self.title


class ReadingList(models.Model):
    """Reading list model."""

    book = models.ForeignKey(
        Book,
        related_name="+",
        verbose_name=_('book'),
        on_delete=models.CASCADE,
        blank=True,
    )
    read = models.BooleanField(
        default=False,
    )
    date_read = models.DateField(
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    def mark_date_read(self):
        """Mark date when book was read."""
        self.date_read = timezone.now()

    def clean_fields(self, exclude=None):
        """Clean the fields needed for django admin."""
        if self.read:
            self.mark_date_read()
        super().clean_fields(exclude=exclude)

    def publish(self):
        """Publish reading list."""
        self.save()

    def __str__(self):
        """Return the string representation."""
        return self.book.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    """Generate authentication API token for a created user instance."""
    if created:
        Token.objects.create(user=instance)
