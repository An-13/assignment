from django.shortcuts import render

# Create your views here.
def boot_web(request):
    return render(request,'boot_web.html')

def forms(request):
    return render(request,'forms.html')

def collapse(request):
    return render(request,'collapse.html')