from django.db import models
import datetime
# Create your models here.
from django.db.models import CharField, TextField, DateField


class Post(models.Model):
    tittle = models.CharField(max_length=100)   # Se puede importar desde modelos
    description = TextField()     # O importando la clase en la parte superior
    image = models.ImageField(upload_to='blog/images/')
    date = DateField(datetime.date.today)
