from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    url = models.URLField(blank=True)

class Resume(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.title
