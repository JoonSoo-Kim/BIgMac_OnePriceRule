import csv

mw=open("Minimum Wage_P.csv", 'r')
fileMatrix_MW=[] ; fileMatrix_csv=[]
csvMW=csv.reader(mw)
for lineContent in csvMW:
    fileMatrix_MW.append(lineContent)

for i in range(2000,2016):
    fileMatrix_temp = [];
    fileMatrix_temp2 = []
    with open(str(i)+'_P.csv', 'r') as fileRead:
        csvRead = csv.reader(fileRead)
        for lineContent in csvRead:
            fileMatrix_temp.append(lineContent)
        for j in range(14):
            fileMatrix_temp2.append(str(float(fileMatrix_MW[j][i-2000]) / float(fileMatrix_temp[j][1])))
        fileMatrix_csv.append(fileMatrix_temp2)

mw.close()

with open('Macjob Index.csv', 'w', newline='') as fileWrite:
    csvWrite = csv.writer(fileWrite)
    for i in range(len(fileMatrix_csv)):
        csvWrite.writerow(fileMatrix_csv[i])