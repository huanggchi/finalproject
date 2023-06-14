from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=100)
    email = forms.EmailField(label='電子郵件')
    message = forms.CharField(label='訊息', widget=forms.Textarea)
