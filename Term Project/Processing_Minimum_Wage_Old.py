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

    for i in range(16):
        fileMatrix_W[0][i] =float(fileMatrix_W[0][i])*1.304758
        fileMatrix_W[1][i] =float(fileMatrix_W[1][i])*3.191389
        fileMatrix_W[2][i] =float(fileMatrix_W[2][i])*0.887397
        fileMatrix_W[3][i] =float(fileMatrix_W[3][i])*1.297737
        fileMatrix_W[4][i] =float(fileMatrix_W[4][i])*648.8338
        fileMatrix_W[5][i] =float(fileMatrix_W[5][i])*23.376333
        fileMatrix_W[6][i] =float(fileMatrix_W[6][i])*274.433333
        fileMatrix_W[7][i] =float(fileMatrix_W[7][i])*112.166141
        fileMatrix_W[8][i] =float(fileMatrix_W[8][i])*18.926517
        fileMatrix_W[9][i] =float(fileMatrix_W[9][i])*1.407408
        fileMatrix_W[10][i] =float(fileMatrix_W[10][i])*3.779333
        fileMatrix_W[11][i] =float(fileMatrix_W[11][i])*58.342801
        fileMatrix_W[12][i] =float(fileMatrix_W[12][i])*1130.424621


with open('Minimum Wage_P.csv', 'w', newline='') as fileWrite:
    csvWrite=csv.writer(fileWrite)
    for i in range(len(fileMatrix_W)):
        csvWrite.writerow(fileMatrix_W[i])

