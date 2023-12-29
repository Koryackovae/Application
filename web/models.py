from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class EventSlotTag(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class EventSlot(models.Model):
    title = models.CharField(max_length=256, verbase_name="Название")
    start_date = models.DateTimeField(verbase_name="Время начала")
    end_date = models.DateTimeField(verbase_name="Время окончания")
    is_realtime = models.BooleanField(default=False, verbase_name="В реальном времени")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbase_name="Пользователь")
    tags = models.ManyToManyField(EventSlotTag, verbase_name="Теги")
    image = models.ImageField(upload_to='event_slots/', null=True, blank=True, verbase_name="Картинка")