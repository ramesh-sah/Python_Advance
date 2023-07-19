from django import forms


class userForms(forms.Form):
    num1 = forms.CharField(label='Value1')
    num2 = forms.CharField(label="Value2")
