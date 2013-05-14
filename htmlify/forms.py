from django import forms


class HtmlifyForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea)
