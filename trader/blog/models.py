from django.db import models

class Post(models.Model):
    """Make a post on the blog."""

    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        """return a string of title data."""
        return self.title
