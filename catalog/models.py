from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, unique= True)
    bio = models.TextField(blank= True, verbose_name="Биогрфия")

    def __str__(self):
        return self.name
