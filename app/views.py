from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
import urllib.parse
import csv
import os


def index(request):
    return redirect(reverse(bus_stations))

with open ('data-398-2018-08-30.csv', 'r', encoding='cp1251') as f:
    reader = csv.DictReader(f)
    CONTENT = [row for row in reader]

    def bus_stations(request):
        page_number = int(request.GET.get("page", 1))
        paginator = Paginator(CONTENT, 10)
        page = paginator.get_page(page_number)
        get_request = page_number+1
        next_page_url = f'{reverse(bus_stations)}?page={get_request}'
        context = {
            'bus_stations': page,
            'current_page': page_number,
            'prev_page_url': None,
            'next_page_url': next_page_url,
        }
        return render(request, 'index.html', context)
