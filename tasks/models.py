from django.db import models
from uuid import uuid4


class Task(models.Model):

    class Meta:
        ordering = ["created_at"]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=80)
    tag = models.CharField(max_length=18)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)