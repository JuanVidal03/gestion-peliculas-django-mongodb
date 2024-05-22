from django.shortcuts import render

# Create your views here.
def incio(request):
    return render(request, "inicio.html")