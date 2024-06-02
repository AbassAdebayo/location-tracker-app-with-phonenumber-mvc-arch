import uuid
from django.db import models
from USERS.MODELS import CustomUser

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='locations')
    area = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.area}, {self.state}, {self.country}"