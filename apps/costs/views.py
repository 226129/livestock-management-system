from django.shortcuts import render

# Create your views here.


def costs(request):
    return render(request, 'costs/costs.html')
