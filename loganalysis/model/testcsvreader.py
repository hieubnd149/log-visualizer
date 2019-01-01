import pandas as pd
import os 


def readlog():
    path = os.path.join(os.getcwd(), '../../upload/access_logs/access_log_20190101.csv')
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


def analyzeByTime(csvlog):
    dateTimes = csvlog['date_time']
    timeData = extractTimeData(dateTimes=dateTimes, mode='h')

    dataFrame = pd.DataFrame(data=timeData, columns=['date_time', 'count'])
    result = dataFrame.groupby(['date_time']).sum()
    # return result
    print(result)


def analyzeByUrl(csvlog):
    print('analyze by url')


csvDataFrame = readlog()
analyzeByTime(csvDataFrame)