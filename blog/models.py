from django.db import models
from django.utils import timezone # para manejar fechas y horas con zona horaria
from django.contrib.auth.models import User # para relacionar post con usuarios

# Create your models here.

# modelo post
class Post(models.Model):
    # campos del modelo Post
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # metodos del modelo
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title