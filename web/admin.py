from django.contrib import admin
from .models import Gallery,Contact
# Register your models here.


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ( 'image',)


# @admin.register(FindPackage)
# class FindPackageAdmin(admin.ModelAdmin):
#     list_display = ( 'destination','persons','date',)


# @admin.register(Destination)
# class DestinationAdmin(admin.ModelAdmin):
#     list_display = ( 'from_place','to_place',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ( 'name','email','subject',)