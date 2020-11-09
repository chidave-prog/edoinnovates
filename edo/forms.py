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

class CommentReplyForm(forms.ModelForm):
    reply = forms.CharField(label="", widget=forms.Textarea(
                                  attrs={
                                      'class': "h6",
                                      'style': 'border-radius: .7em; border: 1px solid #14b3fde3; hover:#14b3fde3;',
                                      'placeholder': 'reply',
                                      'rows': '3',
                                      'cols': '80',
                                  }))

    class Meta:
        model = Comment
        fields = (
            'reply',
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



    