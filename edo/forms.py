from django import forms
from .models import (
                    Contact,
                    Programme,
                    PostView,
                    Comment,
                    Blog,
                    Application,
                    Gallery,
                    Team,
                    Testimony,
                    Newsletter
                    )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ProgrammeForm(forms.ModelForm):
    class Meta:
        model = Programme
        fields = '__all__'

class CommentForm(forms.ModelForm):
    content = forms.CharField(label="Comment", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Type your comment',
            'rows': '4',
            'border': '2px solid #750a20'
        }))

    class Meta:
        model = Comment
        fields = (
            'full_names',
            'phone_number',
            'email',
            'content',
        )


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