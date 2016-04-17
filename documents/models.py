from django.contrib.auth.models import User
from django.db import models


class Document(models.Model):
    identifier = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deadline_at = models.DateTimeField()
    is_incoming = models.BooleanField(default=False)
    is_outbound = models.BooleanField(default=False)
    # doers - исполнители TODO!

    def __str__(self):
        return '[#%s] %s (%s)' % (self.identifier, self.subject, self.author)