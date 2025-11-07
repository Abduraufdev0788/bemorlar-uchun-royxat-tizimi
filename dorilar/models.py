from django.db import models
from users.models import Bemorlar

class Dorilar(models.Model):
    bemor = models.ForeignKey(Bemorlar, on_delete=models.CASCADE, related_name="dorilar")
    dori_name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, help_text="Dori haqida qo‘shimcha izoh")
    once_in_day = models.SmallIntegerField(help_text="Kuniga necha marta ichiladi")
    dosage = models.CharField(max_length=50, help_text="Masalan: 1 dona, 2 ml, 1 tabletka", null=True, blank=True)
    usage_time = models.CharField(max_length=100, help_text="Masalan: Ertalab, Kechqurun, Ovqatdan keyin", null=True, blank=True)
    doctor_name = models.CharField(max_length=100, help_text="Dorini yozgan shifokor", null=True, blank=True)
    created_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    is_active = models.BooleanField(default=True, help_text="Dori ichish muddati tugaganmi yo‘qmi")

    def __str__(self):
        return f"{self.dori_name} ({self.bemor.name})"

