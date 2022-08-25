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