from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
import pytz  # Add this import

class Countdown(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='counters')
    duration_minutes = models.PositiveIntegerField(default=45)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def save(self, *args, **kwargs):
        berlin_tz = pytz.timezone('Europe/Berlin')
        if not self.start_time:
            self.start_time = now().astimezone(berlin_tz)
        self.end_time = self.start_time + timedelta(minutes=self.duration_minutes)
        super().save(*args, **kwargs)

    def time_remaining(self):
        return max((self.end_time - now()).total_seconds(), 0)
