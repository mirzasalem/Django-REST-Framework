from django.db import models

# Create your models here.


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.country_name
    
    
class Person(models.Model):
    country = models.ForeignKey(Country , null= True , blank= True,on_delete=models.CASCADE , related_name= "country")
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    
