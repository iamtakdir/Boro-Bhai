from django.db import models
from django.contrib.auth.models import User

class Source (models.Model):
    title = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Video (models.Model):
    title = models.CharField(max_length=400)
    url = models.URLField()
    youtube_id = models.CharField(max_length=400)
    source = models.ForeignKey(Source,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.title