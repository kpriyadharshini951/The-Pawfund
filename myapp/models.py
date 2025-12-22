from django.db import models

class Donation(models.Model):
    amount = models.IntegerField()  
    donated_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Donation: Rs.{self.amount} at {self.donated_at}"

class Adoption(models.Model):
    dog_name = models.CharField(max_length=50)
    adopter_name = models.CharField(max_length=100)
    adopted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.dog_name} → Adopted by {self.adopter_name}"
