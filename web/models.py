from tabnanny import verbose
from django.db import models
from versatileimagefield.fields import VersatileImageField,PPOIField
# Create your models here.

class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to='gallery/',ppoi_field='ppoi')
    ppoi = PPOIField('Image PPOI')

    class Meta:
        verbose_name_plural = ("Gallery")
    
    def __str__(self):
        return str(self.image)


# class Destination(models.Model):
#     from_place=models.CharField(max_length=225)
#     to_place=models.CharField(max_length=225)

#     class Meta:
#         verbose_name_plural = ("Destination")
    
#     def __str__(self):
#         return str(self.from_place)



# class FindPackage(models.Model):
#     destination=models.ForeignKey(Destination,on_delete=models.CASCADE)
#     persons=models.IntegerField()
#     date=models.DateField()

#     class Meta:
#         verbose_name_plural = ("FindPackage")
    
#     def __str__(self):
#         return str(self.destination)


    
# class Package(models.Model):
#     image = VersatileImageField('Image',upload_to='package/',ppoi_field='ppoi')
#     ppoi = PPOIField('Image PPOI')
#     days=models.CharField(max_length=225)
#     amount=models.IntegerField()

#     class Meta:
#         verbose_name_plural = ("Packages")

#     def __str__(self):
#         return str(self.image)



class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField()

    class Meta:
        verbose_name_plural = ("Contact")

    def __str__(self):
        return self.name   