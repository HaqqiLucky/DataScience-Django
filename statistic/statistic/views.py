from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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

    return render(request, 'home.html', tanggal )


