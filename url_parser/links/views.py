import requests
from bs4 import BeautifulSoup
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import LinkForm


def get_links(url):
    
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    return urls 

def index(request):
    if request.method != 'POST':
        form = LinkForm()
    else:
        form = LinkForm(request.POST or None)
        if form.is_valid():
            return redirect('kek')
    return render(request, 'index.html', {'form':form})

def get_url(request):
    url = request.GET.get('your_url')
    links = get_links(url)
    return render(request, "result.html", {'url':url, 'links':links})
