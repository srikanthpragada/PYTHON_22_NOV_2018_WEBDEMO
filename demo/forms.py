from django import forms
from .models import Job


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class JobForm(forms.Form):
    title = forms.CharField(max_length=30)
    minsal = forms.IntegerField(label='Min Salary')
    maxsal = forms.IntegerField(label='Max Salary')


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'minsal', 'maxsal']
