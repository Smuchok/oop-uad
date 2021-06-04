from django.shortcuts import render, redirect
from .models import Titles
from .forms import TitlesForm
from django.views.generic import DetailView
# Create your views here.



def blog(request):
    blogs = Titles.objects.all().order_by('-date')
    return render(request, 'blog/blog.html', {'blogs': blogs})


class blogInDetales(DetailView):
    model = Titles
    template_name = 'blog/blogInDetails.html'
    context_object_name = 'title'


def add_blog(request):
    error = ''
    if request.method == 'POST':
        form = TitlesForm(request.POST)
        if form.is_valid(): # Перевірка правильності заповнення форми
            form.save()
            return redirect('blog')
        else:
            error = 'Форма заповнена неправильно'

    form = TitlesForm()
    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'blog/add_blog.html', data)