from django.shortcuts import render
from django.http import HttpResponse

def test(request):
    context = {
        'name': 'John'  # Pass any data you want to display in the template
    }
    return render(request, 'test.html', context)
