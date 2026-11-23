from django.db import models
from config import settings


class Status(models.TextChoices):
    TODO = "TODO", "To Do"
    IN_PROGRESS = "IN_PROGRESS", "In Progress"
    DONE = "DONE", "Done"




class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="tasks",)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, default="")
    status = models.CharField(max_length=20,choices=Status.choices, default=Status.TODO,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} ({self.status})"

