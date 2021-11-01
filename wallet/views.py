
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import walletDBForm
from .models import walletDB

# Create your views here.

def home(request):
    
    wallets = walletDB.objects.all()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = walletDBForm(request.POST)
        inpu = form['wallet_address'].value()
        # check whether it's valid:
        #if form.is_valid():
        post = form.save(commit=False)
        post.save()
        
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            #return HttpResponseRedirect('/')
        
    # if a GET (or any other method) we'll create a blank form
    else:
        form = walletDBForm()
    
    #input_ad = request.POST.get('wallet_address')

    return render(request, 'index.html', {'form':form, 'wallets':wallets, 'inpu':inpu})

