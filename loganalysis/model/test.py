import csv

def readLargeFile(datareader, criterion):
    for row in datareader:
        if row[2] == criterion:
            yield row


def processLargeFile(fileName):
    with open(fileName, "rb") as csvfile:
        datareader = csv.reader(csvfile)
        data = []
        
        processor = readLargeFile(datareader, 'POST')
        print('not run yet')

        for row in processor:
            data.append(row)

        for row in data:
            print(row)


processLargeFile('/Users/hieubui/Documents/workspace/python/log-visualizer/upload/access_logs/test_data.csv')

def processMyFile():
    for i in range(3):
        yield i * i
        print('-' + str(i))

myFile = processMyFile()
for m in myFile:
    print(m)