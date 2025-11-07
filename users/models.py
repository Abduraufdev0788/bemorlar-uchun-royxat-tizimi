from django.db import models

class Bemorlar(models.Model):
    gender_choice = {
        "1": "Erkak",
        "2": "Ayol",
    }
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=gender_choice, null= False)
    diagnosis = models.TextField()

    def __str__(self):
        return f"{self.id}. {self.name}  -- {self.diagnosis}"
