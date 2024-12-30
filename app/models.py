from django.db import models

# Create your models here.

class Country(models.Model):
    cou_name=models.CharField(max_length=30,primary_key=True)
    cou_id=models.IntegerField()
    cou_abb=models.CharField(max_length=10)

    def __str__(self):
        return self.cou_name

class Capital(models.Model):
    cou_name=models.OneToOneField(Country,on_delete=models.CASCADE)
    cap_name=models.CharField(max_length=30)
    cap_abb=models.CharField(max_length=10)

    def __str__(self):
        return self.cap_name