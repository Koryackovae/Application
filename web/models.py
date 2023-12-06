from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EventSlotTag(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EventSlot(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_realtime = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(EventSlotTag)
    image = models.ImageField(upload_to='event_slots/', null=True, blank=True)