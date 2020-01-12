from django.shortcuts import (render, get_object_or_404, redirect)
from django.http import  HttpResponse
from .models import ShortUrl
from .forms import UrlForm
from django.views.generic import DetailView

def redirect_page(request, slug):
    url = get_object_or_404(ShortUrl, slug = slug)
    return redirect(url.original_url)

def shorten_url(request):
    if request.method == "POST":
        form = UrlForm(request.POST)

        if form.is_valid():
            original_url = form.cleaned_data['original_url']
            suggested_url_suffix = form.cleaned_data['suggested_url_suffix']
            try:
                f = ShortUrl.objects.create(suggested_url_suffix = suggested_url_suffix, original_url = original_url)
                f.save()
            except ValueError:
                return HttpResponse('Invalid form')
            return redirect(f) 
    else:
        form = UrlForm()
    return render(request, 'urlshortener/home.html', {'form':form})


class UrlDetailView(DetailView):
    model = ShortUrl
    template_name = "urlshortener/success.html"
    context_object_name = "url"



