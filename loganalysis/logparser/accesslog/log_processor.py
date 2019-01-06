import time
import pandas as pd

from .log_reader import read_log, get_use_cols

def get_time_format():
    return {
        'h': '%d/%m/%Y-%H',
        'm': '%d/%m/%Y-%H:%M',
        's': '%d/%m/%Y-%H:%M:%S'
    }

# mode: h - hour, m - minute, s - second
# date time pattern: [dd/MM/YYYY:HH24:MI:SS
def extract_time_from_string(from_date, mode='m'):
    date_format = "[%d/%m/%Y:%H:%M:%S"
    converted = time_format = time.strptime(from_date, date_format)

    extracted_formats = get_time_format()
    return time.strftime(extracted_formats[mode], converted)


def _map_log_date_time(dataFrame):
    dataFrame['date_time'] = dataFrame['date_time'].apply(extract_time_from_string, args=('h'))
    return dataFrame


def _split_req_method_url(request_url):
    (method, url, http) = request_url.split(' ')
    return url


def _map_log_request_method(dataFrame):
    dataFrame['url'] = dataFrame['url'].apply(_split_req_method_url)
    return dataFrame


def _reduce_log_traffic_by_time(dataFrame):
    return dataFrame['date_time'].value_counts()


def _reduce_log_traffic_by_url(dataFrame):
    return dataFrame[['url', 'date_time']].groupby(['url', 'date_time']).size().reset_index(name="count")


def process_access_log():
    mapped_data = read_log(mapFuncs=[_map_log_date_time, _map_log_request_method])
    df = pd.DataFrame(data=mapped_data[0], columns=['ip', 'date_time', 'url', 'response_code', 'response_time'])

    # analyze log
    sr_traffic_by_time = _reduce_log_traffic_by_time(df).sort_index(ascending=True)
    sr_traffic_by_url = _reduce_log_traffic_by_url(df).sort_index(ascending=True)

    return {
        'sr_traffic_by_time': sr_traffic_by_time,
        'sr_traffic_by_url': sr_traffic_by_url
    }