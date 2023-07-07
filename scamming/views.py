from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Collecting
from .forms import CollectingForm




# Create your views here.
def confirming(request):
    return render(request, 'confirmation.html')


def data_collecting(request):
    if request.method == 'POST':
        cform = CollectingForm(request.POST)
        if cform.is_valid():
            cform.save()
            return HttpResponseRedirect('/scamming/confirm/')
    else:
        cform = CollectingForm
    return render(request, 'data_collecting.html', {'cform': cform})


