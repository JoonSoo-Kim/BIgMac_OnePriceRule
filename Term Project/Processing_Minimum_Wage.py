import csv

wanted_country = ['Australia', 'Brazil', 'Canada', 'Chile', 'Czech Republic', 'Hungary', 'Japan', 'South Korea', 'Mexico', 'New Zealand', 'Russia', 'Poland', 'Britain', 'United States']
wanted_country_same = ['Korea', 'Russian Federation', 'United Kingdom']

with open("Minimum Wage.csv", 'r', encoding='UTF8') as wagefile:
    fileMatrix=[]
    fileMatrix_temp=[]
    fileMatrix_W=[]
    csvWage=csv.reader(wagefile)

    for lineContext in csvWage:
        fileMatrix.append(lineContext)
    for i in range(len(fileMatrix)):
        if (fileMatrix[i][1] in wanted_country) or (fileMatrix[i][1] in wanted_country_same):
            fileMatrix_temp.append(fileMatrix[i][14])

    j=0
    while True:
        if j == len(fileMatrix_temp):
            break
        zero_to_fifteen=fileMatrix_temp[j:j+16]
        fileMatrix_W.append(zero_to_fifteen)
        j+=16

    fileMatrix_temp2=[]
    for i in range(2000,2016):
        fileMatrix_temp2 = []
        with open(str(i)+'_P.csv', 'r') as fileEX:
            csvEX = csv.reader(fileEX)
            for lineContext in csvEX:
                fileMatrix_temp2.append(lineContext)
        fileMatrix_W[0][i-2000] =float(fileMatrix_W[0][i-2000])*float(fileMatrix_temp2[0][2])
        fileMatrix_W[1][i-2000] =float(fileMatrix_W[1][i-2000])*float(fileMatrix_temp2[1][2])
        fileMatrix_W[2][i-2000] =float(fileMatrix_W[2][i-2000])*float(fileMatrix_temp2[2][2])
        fileMatrix_W[3][i-2000] =float(fileMatrix_W[3][i-2000])*float(fileMatrix_temp2[3][2])
        fileMatrix_W[4][i-2000] =float(fileMatrix_W[4][i-2000])*float(fileMatrix_temp2[4][2])
        fileMatrix_W[5][i-2000] =float(fileMatrix_W[5][i-2000])*float(fileMatrix_temp2[5][2])
        fileMatrix_W[6][i-2000] =float(fileMatrix_W[6][i-2000])*float(fileMatrix_temp2[6][2])
        fileMatrix_W[7][i-2000] =float(fileMatrix_W[7][i-2000])*float(fileMatrix_temp2[7][2])
        fileMatrix_W[8][i-2000] =float(fileMatrix_W[8][i-2000])*float(fileMatrix_temp2[8][2])
        fileMatrix_W[9][i-2000] =float(fileMatrix_W[9][i-2000])*float(fileMatrix_temp2[9][2])
        fileMatrix_W[10][i-2000] =float(fileMatrix_W[10][i-2000])*float(fileMatrix_temp2[10][2])
        fileMatrix_W[11][i-2000] =float(fileMatrix_W[11][i-2000])*float(fileMatrix_temp2[11][2])
        fileMatrix_W[12][i-2000] =float(fileMatrix_W[12][i-2000])*float(fileMatrix_temp2[12][2])


with open('Minimum Wage_P.csv', 'w', newline='') as fileWrite:
    csvWrite=csv.writer(fileWrite)
    for i in range(len(fileMatrix_W)):
        csvWrite.writerow(fileMatrix_W[i])