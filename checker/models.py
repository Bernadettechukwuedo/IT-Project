from django.db import models


# Create your models here.
class Ping(models.Model):
    url = models.CharField(max_length=225, verbose_name="Ip address or Domain name ")
    status = models.CharField(max_length=225)

    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} : {self.status} : {self.timestamp}"
