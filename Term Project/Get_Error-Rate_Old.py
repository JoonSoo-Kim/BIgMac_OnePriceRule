import csv

class exchange:
    def __init__(self, givenPL, givenPU, exRateR):
        self.price_Local=givenPL
        self.price_USA=givenPU
        self.exchange_Real=exRateR
        self.exchange_Fake=givenPL/givenPU

    def errorRate(self):
        return (self.exchange_Fake-self.exchange_Real)/self.exchange_Real*100

errorRate=[]

#2001
fileMatrix=[]; errorRate_2001=[2001]
with open("2001_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2001.append(ToDo.errorRate())

errorRate.append(errorRate_2001)

#2002
fileMatrix=[]; errorRate_2002=[2002]
with open("2002_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2002.append(ToDo.errorRate())

errorRate.append(errorRate_2002)

#2003
fileMatrix=[]; errorRate_2003=[2003]
with open("2003_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2003.append(ToDo.errorRate())

errorRate.append(errorRate_2003)

#2004
fileMatrix=[]; errorRate_2004=[2004]
with open("2004_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2004.append(ToDo.errorRate())

errorRate.append(errorRate_2004)

#2005
fileMatrix=[]; errorRate_2005=[2005]
with open("2005_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2005.append(ToDo.errorRate())

errorRate.append(errorRate_2005)

#2006
fileMatrix=[]; errorRate_2006=[2006]
with open("2006_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2006.append(ToDo.errorRate())

errorRate.append(errorRate_2006)

#2007
fileMatrix=[]; errorRate_2007=[2007]
with open("2007_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2007.append(ToDo.errorRate())

errorRate.append(errorRate_2007)

#2008
fileMatrix=[]; errorRate_2008=[2008]
with open("2008_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2008.append(ToDo.errorRate())

errorRate.append(errorRate_2008)

#2009
fileMatrix=[]; errorRate_2009=[2009]
with open("2009_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2009.append(ToDo.errorRate())

errorRate.append(errorRate_2009)

#2010
fileMatrix=[]; errorRate_2010=[2010]
with open("2010_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2010.append(ToDo.errorRate())

errorRate.append(errorRate_2010)

#2011
fileMatrix=[]; errorRate_2011=[2011]
with open("2011_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2011.append(ToDo.errorRate())

errorRate.append(errorRate_2011)

#2012
fileMatrix=[]; errorRate_2012=[2012]
with open("2012_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2012.append(ToDo.errorRate())

errorRate.append(errorRate_2012)

#2013
fileMatrix=[]; errorRate_2013=[2013]
with open("2013_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2013.append(ToDo.errorRate())

errorRate.append(errorRate_2013)

#2014
fileMatrix=[]; errorRate_2014=[2014]
with open("2014_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2014.append(ToDo.errorRate())

errorRate.append(errorRate_2014)

#2015
fileMatrix=[]; errorRate_2015=[2015]
with open("2015_P.csv", 'r') as fileRead:
    csvFile = csv.reader(fileRead)
    for lineContent in csvFile:
        fileMatrix.append(lineContent)

lenfileMatrix=len(fileMatrix)
price_in_USA=float(fileMatrix[-1][1])

for i in range(lenfileMatrix-1):
    ToDo=exchange(float(fileMatrix[i][1]), price_in_USA, float(fileMatrix[i][2]))
    errorRate_2015.append(ToDo.errorRate())

errorRate.append(errorRate_2015)

#errorRate
with open('Error Rate.csv', 'w', newline='') as fileWrite:
    csvWrite=csv.writer(fileWrite)
    for i in range(len(errorRate)):
        csvWrite.writerow(errorRate[i])