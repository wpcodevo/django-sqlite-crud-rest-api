import uuid
from django.db import models


class FeedbackModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    feedback = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=255)
    rating = models.FloatField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "feedback"
        ordering = ['-createdAt']

    def __str__(self) -> str:
        return self.name
