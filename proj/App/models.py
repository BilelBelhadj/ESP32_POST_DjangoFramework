from django.db import models

class Obj(models.Model):
    nameMicro = models.fields.CharField(max_length=100)
    nameCapteur = models.fields.CharField(max_length=100)
    donnee = models.fields.CharField(max_length=100)