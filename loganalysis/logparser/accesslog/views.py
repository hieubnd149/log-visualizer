from django.shortcuts import render
from django.http import HttpResponse

from .logreader import readlog, analyzeTimeHourTraffic, analyzeURLTraffic

def processAccessLog(request):
    accesslog = readlog()
    hourTrafficAnalyzedData = analyzeTimeHourTraffic(accesslog)
    urlTrafficAnalyzedData = analyzeURLTraffic(accesslog)

    context = {
        'hourTrafficAnalyzedData': hourTrafficAnalyzedData.to_json(orient='index'),
        'urlTrafficAnalyzedData': urlTrafficAnalyzedData.to_json(orient='table')
    }
    return render(request, 'logparser/logview.html', context)
