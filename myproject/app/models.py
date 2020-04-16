
from django.db import models


class data(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=999)
class log_res(models.Model):
    id_page = models.CharField(max_length=50)
    res = models.CharField(max_length=99999)
    Statut_res = models.CharField(max_length=10)
    star_date =  models.DateTimeField()
    stop_date =  models.DateTimeField()