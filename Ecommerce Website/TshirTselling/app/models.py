from django.db import models

# Create your models here.




class Product(models.Model):
    name=models.CharField(max_length=100)
    catogery=models.CharField(max_length=100)
    image=models.ImageField(upload_to='media')
    price=models.IntegerField()
    description=models.TextField(max_length=2000)
    
    
    
    
    def __str__(self):
        return self.name