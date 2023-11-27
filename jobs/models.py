from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    jobTitle = models.CharField(max_length=200)
    companyName = models.CharField(max_length=100)
    description = models.TextField(max_length=15000, null=True, blank=True, default='')
    cvFile = models.FileField(upload_to='upload')
    coverLetterFile = models.FileField(upload_to='upload', blank=True)
    applicationDate = models.DateField(auto_now_add=True)
    feedback = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-applicationDate']

