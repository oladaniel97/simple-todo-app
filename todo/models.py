from django.db import models

# Create your models here.
class Todo(models.Model):
    item = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item

    class Meta:
        ordering =('-date_added',)