from django.db import models
from django.utils import timezone
import uuid
import datetime
# Create your models here.

class Weather(models.Model):
    
    id = models.UUIDField(
        default=uuid.uuid4,
        unique= True,
        editable=False,
        primary_key=True,
        )    
    icon = models.CharField(max_length=255,default='')
    temp_c = models.DecimalField(max_digits=5,decimal_places=2,default=00.00)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    date = models.CharField(max_length=255,default=datetime.date.today())
    #Nie wiem do końca czy to jest potrzebne ale wrzucam
    def save(self, **kwargs):
        super().save(**kwargs)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def __str__(self):
        return super().__str__()
    