from distutils.command.upload import upload
from django.db import models

class Offer (models.Model):
    hotel_name = models.CharField(max_length=50)
    localization= models.CharField(max_length=70)
    stars_number= models.ImageField()
    
    price=models.FloatField()
    image= models.ImageField(upload_to= 'photos/%y/%m/%d')


    
def __str__(self):
    return self.name 

#def Meta() :
    #permission=[('can add new offer')]