from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'homepage/home.html')

def contact(request):
    return render(request, 'homepage/basic.html', {'content': [
    'This is the Contact Form',
    'Author: @Ruckusist <ruckusist@alphagriffin.com>'
    ]})
