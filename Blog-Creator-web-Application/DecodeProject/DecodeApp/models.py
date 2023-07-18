from django.db import models

from datetime import date

from django.conf import settings

from ckeditor_uploader.fields import RichTextUploadingField


    
    
#admin details   fields   

class User(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    upassword=models.CharField(max_length=100)
    
    def __str__(self):
        return self.uname
    
    
    
    
    
#user query model fields
class QuerySend(models.Model):
    uname=models.CharField(max_length=100)
    uemail=models.EmailField()
    query=models.TextField()
    
    def __str__(self):
        return self.uname
    
    
    
    
    
    
 #blog models fields   
class Blog(models.Model):
    image=models.ImageField(upload_to='images/')
    title=models.CharField(max_length=200)
    Catogery=models.CharField(max_length=200)
    description=RichTextUploadingField()
    postedDate=models.DateField(default=date.today())
    good_name=models.CharField(max_length=200)
    view = models.IntegerField(default=0)
    
    
    def __str__(self):
        return self.title
    
