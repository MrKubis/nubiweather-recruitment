from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class Weather(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique= True,
        primary_key = True,
        editable=False
        )
    icon = models.CharField(max_length=255,default='')
    temp_c = models.DecimalField(max_digits=5,decimal_places=2,default=00.00)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    #To wklepuje tutaj bo czasem bez tego nie działa xddd
    def save(self, **kwargs):
        super().save(**kwargs)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self):
        return super().__str__()
    