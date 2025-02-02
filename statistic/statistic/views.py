from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .api_service import get_quotes

def homepage(request) :
    now = datetime.now()
    now_format = now.strftime("%Y-%m-%d")
    day_format = now.strftime("%A")
    time_format = now.strftime("%H:%M:%S")

    tanggal = {
        "date" : now_format,
        "day" : day_format,
        "time": time_format
    }

    return render(request, 'layout.html', tanggal )

def test(request):
    return render(request,'test.html')

def random_quotes(request):
    random_quote_data = get_quotes()
    return render(request, 'layout.html', {"quote":random_quote_data})


