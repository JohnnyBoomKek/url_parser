import requests
from bs4 import BeautifulSoup
from django.core.validators import URLValidator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.forms import ValidationError
from .forms import LinkForm
from .tables import LinkTable, UrlTable
import aiohttp
import asyncio
import json
validate = URLValidator()

def index(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            urls = get_all_links(url)
            #Асинхнонная функция реализована и готова к бою. К сожалению указаный API не возращает ожидаемые данные.
            #Поэтому на данном этапе ограничусь парсером всех валидных url
            #data = asyncio.run(main(urls))
            data = [{'url':value} for value in urls]
            table = UrlTable(data=data)
            return render(request, 'index.html', {'form':form, 'table':table})
    else:
        form = LinkForm()
    return render(request, 'index.html', {'form':form})

def get_all_links(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    anchors = soup.find_all('a')
    urls = []
    for anchor in anchors:
        link = anchor.get('href')
        try:
            validate(link)
            urls.append(link)
        except ValidationError:
            pass
    return urls


async def get_url_info(url, session):
    async with session.get(url) as response:
        data = await response.read()
        return json.loads(data.decode('utf-8'))

async def main(links):
    url = 'https://api.domainsdb.info/v1/domains/search?domain='
    tasks = []

    async with aiohttp.ClientSession() as session:
        for link in links:
            task = asyncio.create_task(get_url_info(url+link, session))
            tasks.append(task)

        await asyncio.gather(*tasks)
        return [task.result() for task in tasks]




