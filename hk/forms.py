from django import forms


class EmailForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())



class BinanceEmail(forms.Form):
    email = forms.EmailField()
    

class BinancePassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())