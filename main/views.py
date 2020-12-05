from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
    
def index_ru(request):
    return render(request, 'index_ru.html')
    
    