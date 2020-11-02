from django import forms
from .models import (Contact,
                    Programme,
                    Application
                    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = '__all__'

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields =  ('programme',
                'first_name',
                'last_name',
                'gender',
                'email',
                'phone_number',
                'address',)