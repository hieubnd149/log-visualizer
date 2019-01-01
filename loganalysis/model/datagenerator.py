#10.136.64.155 - - [08/Dec/2018:07:00:05 +0700] "POST /cinox/ws/CommonRestService/getUserApiData HTTP/1.1" 200 148 "-" "-"
import random
import time
from datetime import date

ipaddresses = [
    '202.200.113.6',
    '224.86.133.136',
    '189.87.207.213',
    '144.147.210.55',
    '224.146.89.240',
    '101.49.150.19',
    '220.135.167.72',
    '100.144.47.166',
    '113.255.96.94',
    '202.129.214.41'
]

urls = [
    '/cinox/ws/CommonRestService/getUserApiData HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData1 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData2 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData3 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData4 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData5 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData6 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData7 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData8 HTTP/1.1',
    '/cinox/ws/CommonRestService/getUserApiData9 HTTP/1.1'
]

requestMethods = [
    'GET',
    'POST',
    'PUT',
    'DELETE'
]

TOTAL_GENERATED = 1000

today = date.today()
date1 = (today.year, 1, 1, 0, 0, 0, -1, -1, -1)
startDt = time.mktime(date1)
date2 = (today.year, 1, 1, 23, 59, 59, -1, -1, -1)
endDt = time.mktime(date2)

openFile = open('access_log_20190101.csv', 'w')

for _ in range(0, TOTAL_GENERATED):
    # write access log here
    randIP = random.randint(0, len(ipaddresses) - 1)
    randURL = random.randint(0, len(urls) - 1)
    randMethod = random.randint(0, len(requestMethods) - 1)
    random_time = time.localtime(random.uniform(startDt, endDt))

    row = ipaddresses[randIP] + ' - - [' + time.strftime("%d/%m/%Y:%H:%M:%S", random_time) +  ' +0700] "'
    row += requestMethods[randMethod] + ' ' + urls[randURL] + '" 200 ' + str(random.randint(100, 1000)) + ' "-" "-"'
    row += '\n'

    openFile.write(row)

openFile.close()