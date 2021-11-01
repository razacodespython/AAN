from django import forms
from django.forms import fields, ModelForm
from django import forms
from .models import walletDB

class walletDBForm(forms.ModelForm):
    class Meta:
        model = walletDB
        fields = ['wallet_address','private_key','nft_contract']


