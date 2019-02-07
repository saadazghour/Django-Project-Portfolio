from django.db import models
from datetime import datetime


"""

step by step to create blog app

1-- Create a blog models
2-- Add the Blog models to the settings (blog app )
3-- makemigrations
4-- migrate
5-- Add the models (Blog) to the admin

"""


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=400)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(blank=True)


    def __str__(self):
        return self.title


    def showing_description(self):
        return self.description[:159]