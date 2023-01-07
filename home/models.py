from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=122)
    date = models.DateField()
    
class Vet(models.Model):
    name=models.CharField(max_length=100)
    Contact_info=models.DecimalField(max_digits=10,decimal_places=0)
    Address=models.CharField(max_length=100)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    
class Trainer(models.Model):
    name=models.CharField(max_length=100)
    Contact_info=models.DecimalField(max_digits=10,decimal_places=0)
    Address=models.CharField(max_length=100)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    
class Dog_info(models.Model):
    name=models.CharField(max_length=100)
    breed=models.CharField(max_length=100)
    medication=models.CharField(max_length=100)
    food=models.CharField(max_length=100)
    License_and_Insaurance=models.CharField(max_length=100)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    
class Places(models.Model):
    name=models.CharField(max_length=100)
    Open_time=models.TimeField()
    Close_time=models.TimeField()
    Address=models.CharField(max_length=100)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    
class Product(models.Model):
    id=models.DecimalField(max_digits=10,decimal_places=0,primary_key=True)
    name=models.CharField(max_length=100)
    Price=models.DecimalField(max_digits=10,decimal_places=0)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
    
class Breed_info(models.Model):
    name=models.CharField(max_length=100)
    information=models.CharField(max_length=100000)
    link=models.CharField(max_length=1000)
    def __str__(self):
        return f"{self.name}"
