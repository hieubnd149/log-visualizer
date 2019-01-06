import pandas as pd
import os 
from os.path import join, isfile


def _get_indexes():
    return ['ip', 'None_1', 'None_2', 'date_time', 'time_zone', 'url', 'response_code', 'response_time', 'none_3', 'none_4']


def get_use_cols():
    return ['ip', 'date_time', 'url', 'response_code', 'response_time']


def _chunk_generator(filename, chunkSize=10 ** 5):
    for chunk in pd.read_csv(filename, chunksize=chunkSize, iterator=True, names=_get_indexes(), sep=' ', usecols=get_use_cols()):
        yield chunk

    
def _generator(filename, chunkSize=10 ** 5):
    chunk = _chunk_generator(filename, chunkSize=chunkSize)
    for row in chunk:
        yield row


def read_log(mapFuncs=None, filterFuncs=None):
    logPath = '../upload/access_logs/'
    files = [f for f in os.listdir(logPath) if isfile(join(logPath, f)) and f.find('access_log') == 0]

    data = []

    for f in files:
        generator = _generator(join(logPath, f))
        row = ''
        while(row is not None):
            row = next(generator, None)

            if row is not None:
                # apply map function
                if mapFuncs is not None:
                    for func in mapFuncs:
                        row = func(row)

                # apply filter function
                if filterFuncs is not None:
                    for func in filterFuncs:
                        row = func(row)

                data.append(row)
    
    return data

