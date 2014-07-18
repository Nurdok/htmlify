from django import forms


class HtmlifyForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)
    CHOICES = ( ('ASCII', 'ASCII'), ('UTF-8', 'UTF-8')) 
    encoding = forms.ChoiceField(choices=CHOICES, widget=forms.Select())