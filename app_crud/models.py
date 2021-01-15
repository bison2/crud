from django.db import models
from django.conf import settings
from django.db.models import CASCADE

from django.urls import reverse
# Create your models here.


class Pessoa(models.Model):
    
    nome = models.CharField(max_length=100)
    slug = models.SlugField(blank = True)

    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('app_crud:pessoa', args=[self.id])
        #return reverse('app_crud:pessoa', kwargs={'id': self.id})

