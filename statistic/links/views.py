from django.shortcuts import render
from .models import Link
from django.http import HttpResponse

# Create your views here.

def link_list(request):
    links = Link.objects.all().order_by('-tgl_dipublish')
    return render(request, 'links/links_list.html', {'links' : links})

def link_page(request, slug):
    link = Link.objects.get(slug=slug)
    return render(request, 'links/link_page.html', {'link' : link})
    # return HttpResponse(slug)