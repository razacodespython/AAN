from django.db import models

# Create your models here.

class walletDB(models.Model):
    wallet_address = models.CharField(max_length=20000)
    private_key = models.CharField(max_length=20000)
    nft_contract = models.CharField(max_length=20000)

def __str__(self):
    return self.wallet_address