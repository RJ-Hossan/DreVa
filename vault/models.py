from django.db import models
from django.contrib.auth.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    target_date = models.DateField()
    progress = models.IntegerField(default=0)  # Percentage of completion

    def __str__(self):
        return self.title

class Dream(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    interpretation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class EventTimeCapsule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    messages = models.TextField(blank=True)
    unlocked = models.BooleanField(default=False)

    def __str__(self):
        return self.event_name
