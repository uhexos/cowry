import uuid
from django.db import models

class KeyValuePair(models.Model):
    key = models.DateTimeField(auto_now_add=True)
    value = models.UUIDField(default=uuid.uuid4)