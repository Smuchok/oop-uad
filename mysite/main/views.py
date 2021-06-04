from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_page(request):
    # return HttpResponse("<h1>Головна. Hello world</h1>" + "<a href='/about'>Про нас</a>")
    return render(request, 'main/main_page.html')

def about(request):
    # return HttpResponse('<h1>Про нас</h1>')
    return render(request, 'main/about.html')

# def blog(request):
#     return render(request, 'main/blog.html')
