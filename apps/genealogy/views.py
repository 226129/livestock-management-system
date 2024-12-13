from django.shortcuts import render

# Create your views here.


def genealogy(request):
    return render(request, 'genealogy/genealogy.html')
