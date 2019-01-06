from django.shortcuts import render
from django.http import HttpResponse

from .log_processor import process_access_log

def processAccessLog(request):
    access_log_data = process_access_log()

    context = {
        'sr_traffic_by_time': access_log_data['sr_traffic_by_time'].to_json(orient='index'),
        'sr_traffic_by_url': access_log_data['sr_traffic_by_url'].to_json(orient='table'),
    }

    return render(request, 'logparser/logview.html', context)

