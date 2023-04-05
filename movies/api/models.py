from django.db import models

# Create your models here.

movies=[
    {"id":1,"name":"Sphadikam","year":1996,"director":"Bhadran","genre":"drama"},
    {"id":2,"name":"premam","year":2017,"director":"alphones","genre":"romance"},
    {"id":3,"name":"lucifer","year":2019,"director":"prithwiraj","genre":"action"},
    {"id":4,"name":"Iron Man","year":2008,"director":"John Favru","genre":"action"},
    {"id":5,"name":"DSMM","year":2022,"director":"Sam Raimi","genre":"fantacy"},
]

class Movies(models.Model):
    name=models.CharField(max_length=100)
    year=models.IntegerField()
    director=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    