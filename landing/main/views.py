from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from .forms import LeadForm # mer hargarjan formy

# Create your views here.

def index(request: HttpRequest):
    if request.method == 'POST': # ete post a
        form = LeadForm(request.POST) # user axperi uxarkac /POST/-i tvyalneri himan vra sarqum
                                      # enq form u heto el stugum chisht a uxarke te che braty

        if form.is_valid(): # ete chisht a uxarke axpery
            form.save() # pahum enq
            messages.success(request, 'Abri axpery, chisht es xrge gandz, esa knayem namakd.')
        else: # ete ed tuften sxal a xrge
            messages.error(request, 'Lav ches ara, hly dzi nor xrgi ay fucn.')

        return redirect(reverse('index') + '#contact') # maqrum enq exac chexacy vor noric
                                                       # chxrgi axpery vor nuyn banic hazar hat chunenanq                                                   
    else: # ete get zapros a
        return render(request, 'main/index.html')
    