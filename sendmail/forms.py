from django import forms

class SendMailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    receiver = forms.EmailField()