import pandas as pd
import csv


wanted_country = ['Australia', 'Brazil', 'Canada', 'Chile', 'Czech Republic', 'Hungary', 'Japan', 'South Korea', 'Mexico', 'New Zealand', 'Russia', 'Poland', 'Britain', 'United States']

for i in range(2000,2016):
    data_file_temp = pd.read_html('http://bigmacindex.org/'+str(i)+'-big-mac-index.html', flavor='html5lib')
    data_file = data_file_temp[0]

    data_file.to_csv(str(i)+".csv", mode='w', header=False)

    fileMatrix=[] ; fileMatrix_result = []

    with open(str(i)+".csv", 'r') as fileRead:

        csvFile = csv.reader(fileRead)

        for lineContent in csvFile:
            fileMatrix.append(lineContent)

        for j in range(len(fileMatrix)):
            fileMatrix[j] = fileMatrix[j][1:4]
            if fileMatrix[j][0] in wanted_country:
                fileMatrix_result.append(fileMatrix[j])

    with open(str(i)+"_P.csv", 'w', newline='') as fileWrite:

        csvFile2=csv.writer(fileWrite)

        for k in range(len(fileMatrix_result)):
            csvFile2.writerow(fileMatrix_result[k])