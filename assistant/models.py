from django.db import models
from django.conf import settings


class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Game(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    release = models.DateField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Word(models.Model):
    game = models.ForeignKey(Game, related_name="words", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="user_words", on_delete=models.PROTECT)
    word_en = models.CharField(max_length=50)
    word_ru = models.CharField(max_length=50)
    definition = models.TextField()
    image = models.ImageField(upload_to='media/Word/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.word_en} - {self.word_ru}'


class Correction(models.Model):
    word = models.ForeignKey(Word, related_name="corrections", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="corrections", on_delete=models.PROTECT)
    definition = models.TextField()
    image = models.ImageField(upload_to='media/Word/', blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.word}'
