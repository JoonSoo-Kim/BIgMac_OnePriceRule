import csv

def getErrorRate(Price_Local, Price_USA, exchangeRate_Real):
    exchangeRate_Fake=Price_Local/Price_USA
    return (exchangeRate_Fake - exchangeRate_Real)/exchangeRate_Real*100

errorRate_result=[]
for i in range(2000,2016):
    fileMatrix = []
    errorRate_temp = [i]

    with open(str(i)+"_P.csv", 'r') as fileRead:
        csvFile = csv.reader(fileRead)
        for lineContent in csvFile:
            fileMatrix.append(lineContent)

    price_in_USA = float(fileMatrix[-1][1])
    for j in range(len(fileMatrix) - 1):
        errorRate_temp.append(getErrorRate(float(fileMatrix[j][1]), price_in_USA, float(fileMatrix[j][2])))
    errorRate_result.append(errorRate_temp)

with open('Error Rate.csv', 'w', newline='') as fileWrite:
    csvWrite=csv.writer(fileWrite)
    for i in range(len(errorRate_result)):
        csvWrite.writerow(errorRate_result[i])