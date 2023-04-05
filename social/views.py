from django.shortcuts import render


# Create your views here.

def socialIndex(request):
    index = ""
    return render(request, '../templates/social/socialIndex.html', {'index': index})
