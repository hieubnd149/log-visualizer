import pandas as pd
import os 


def readlog():
    path = os.path.join(os.getcwd(), '../upload/access_logs/access_log_20190101.csv')
    indexes = ['ip', 'None_1', 'None_2', 'date_time', 'time_zone', 'url', 'response_code', 'response_time', 'none_3', 'none_4']
    
    # read access log
    # one by one
    accesslog = pd.read_csv(path, names=indexes, sep=' ')
    return accesslog


# mode: h - hour, m - minute, s - second
# date time pattern: [dd/MM/YYYY:HH24:MI:SS
def extractTimeData(dateTimes, mode='m'):
    toIndex = 20 #default for s
    postFix = ''

    if mode == 'm':
        toIndex = 17
        postFix = ':00'
    elif mode == 'h':
        toIndex = 14
        postFix = ':00:00'
    
    times = [(elem[1:toIndex] + postFix, 1) for elem in dateTimes]
    return times


def analyzeTimeHourTraffic(csvlog):
    dateTimes = csvlog['date_time']
    timeData = extractTimeData(dateTimes=dateTimes, mode='h')

    dataFrame = pd.DataFrame(data=timeData, columns=['date_time', 'count'])
    result = dataFrame.groupby(['date_time']).sum()
    return result


def extractUrlSeriesData(urls):
    # pattern: "POST /cinox/ws/CommonRestService/getUserApiData5 HTTP/1.1"
    urlSeries = []
    for fullUrl in urls:
        arr = fullUrl.split(" ")
        urlSeries.append((arr[0], arr[1], 1))
    return urlSeries


def analyzeURLTraffic(csvlog):
    urls = csvlog['url']
    urlSeries = extractUrlSeriesData(urls=urls)

    dataFrame = pd.DataFrame(data=urlSeries, columns=['method', 'url', 'count'])
    result = dataFrame.groupby(['url', 'method']).sum()
    return result

