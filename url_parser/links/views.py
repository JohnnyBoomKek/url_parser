import requests
from bs4 import BeautifulSoup
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.forms import ValidationError
from .forms import LinkForm
from .tables import LinkTable
import aiohttp
import asyncio
validate = URLValidator()

def index(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            links = get_links(url)
            asyncio.run(get_links(links))
            return render(request, 'index.html', {'form':form, 'links':links})
    else:
        form = LinkForm()
    return render(request, 'index.html', {'form':form})

def get_links(url):
    links = []
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    anchors = soup.find_all('a')
    for anchor in anchors:
        link = anchor.get('href')
        try:
            validate(link)
            links.append(link)
        except ValidationError:
            pass
    return links

async def get_data(url, session):
    async with session.get(url) as response:
        data = await response.read()
        print(data)

async def links_info(links:list):
    url = 'https://api.domainsdb.info/v1/domains/search?domain='
    tasks = []

    async with aiohttp.ClientSession() as session:
        for link in links:
            print(link)
            task = asyncio.create_task(get_data(f'https://api.domainsdb.info/v1/domains/search?domain={link}', session))
            task.append(task)
        
        await asyncio.gather(*tasks)