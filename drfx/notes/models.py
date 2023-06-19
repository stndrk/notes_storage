from django.db import models
from django.conf import settings
from utils.models import TimeStampedModel

class Notes(TimeStampedModel):
    TYPE_CHOICES = [
        ('audio', 'Audio'),
        ('video', 'Video'),
        ('text', 'Text'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    note_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    audio_file = models.FileField(upload_to='notes/audio/', null=True, blank=True)
    video_file = models.FileField(upload_to='notes/video/', null=True, blank=True)
    text_content = models.TextField(null=True, blank=True)
