import numpy as np
import matplotlib.pyplot as plt
import csv

yearInput=int(input("Year : "))

fileMatrix = []
with open('Error Rate.csv', 'r') as fileRead:
    csvFirst=csv.reader(fileRead)
    for i in csvFirst:
        fileMatrix.append(i)

y_rate=[]
for i in range(len(fileMatrix[yearInput-2001])-1):
    y_rate.append(float(fileMatrix[yearInput-2001][i+1]))

x_country=['AUS', 'BRA', 'UK', 'CAN', 'CHL', 'CZE', 'HUN', 'JPN', 'MEX', 'NZL', 'POL', 'RUS', 'KOR'c]

N_of_groups = len(x_country)
index = np.arange(N_of_groups)

plt.bar(index, y_rate, tick_label=x_country, align='center')

plt.xlabel('Country')
plt.ylabel('Error Rate (%) ')
plt.title('Error Rate in '+str(yearInput))
plt.xlim( -1, N_of_groups)
plt.ylim( -100, 100)
fig = plt.gcf()
plt.show()

bar_width = 0.2
opacity = 0.5

plt.bar(index, y_rate, bar_width, tick_label=x_country, align='center',alpha=opacity, color='b', label='year')
fig.savefig('Chart_'+str(yearInput)+'.png')