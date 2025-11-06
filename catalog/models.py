from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, unique= True)
    bio = models.TextField(blank= True, verbose_name="Биография")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Артист"
        verbose_name_plural = "Артисты"

class Release(models.Model):
    TYPE_CHOICES = [
        ('album', 'Альбом'),
        ('ep', 'EP'),
        ('single', 'Сингл')
    ]

    title = models.CharField(max_length=200, verbose_name="Название")
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='releases')
    release_type = models.CharField(max_length=10, choices= TYPE_CHOICES,default='album', verbose_name="Тип")
    cover = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Обложка")
    release_date = models.DateField(verbose_name="Дата релиза")
    description = models.TextField(blank=True,verbose_name="Описание")

    def __str__(self):
        return f"{self.artist.name} - {self.title}"

    class Meta:
        verbose_name = "Релиз"
        verbose_name_plural = "Релизы"
        ordering = ['-release_date']