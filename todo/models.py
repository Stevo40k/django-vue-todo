from django.db import models

# Create your models here.
class ToDo(models.Model):
    text = models.CharField(max_length=255, default='')
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.text
