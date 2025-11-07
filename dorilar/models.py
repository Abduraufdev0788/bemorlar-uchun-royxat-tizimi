from django.db import models
from users.models import Bemorlar

class Dorilar(models.Model):
    bemor_id = models.ForeignKey(Bemorlar, on_delete=models.CASCADE)
    dori_name = models.CharField(max_length=100)
    description = models.TextField()
    med_time = models.DateTimeField()

    def __str__(self):
        return f"{self.bemor_id}. {self.dori_name} - {self.med_time}"
