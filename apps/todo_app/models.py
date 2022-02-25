from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Folder(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.title}"


class Task(models.Model):

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    title = models.CharField(max_length=300, blank=False, null=False)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.title}  -  {self.is_completed}"
