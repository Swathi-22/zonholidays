from django import forms
from .models import Contact
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'
        widgets={
            'name':TextInput(attrs={'placeholder':"Your Name",'id':"name",'class':" required"}),
            'email':EmailInput(attrs={'placeholder':"Your Email",'id':"email",'class':"required"}),
            'phone':TextInput(attrs={'placeholder':"Your Phone",'id':"phone",'class':"required"}),
            'subject':TextInput(attrs={'placeholder':"Subject",'id':"subject",}),
            'message':Textarea(attrs={'placeholder':"Comment",'id':"message",'rows':"6"}),
         }