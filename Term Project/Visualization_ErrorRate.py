import numpy as np
import matplotlib.pyplot as plt
import csv

def which_Country(countryInput):
    if countryInput == "Australia":
        return 1
    elif countryInput == "Brazil":
        return 2
    elif countryInput == "Britain" or countryInput == "United Kingdom":
        return 3
    elif countryInput == "Canada":
        return 4
    elif countryInput == "Chile":
        return 5
    elif countryInput == "Czech Republic":
        return 6
    elif countryInput == "Hungary":
        return 7
    elif countryInput == "Japan":
        return 8
    elif countryInput == "Mexico":
        return 9
    elif countryInput == "New Zealand":
        return 10
    elif countryInput == "Poland":
        return 11
    elif countryInput == "Russia":
        return 12
    elif countryInput == "South Korea" or countryInput == "Korea":
        return 13

selectNum=int(input("1. 연도별  |  2. 국가별  :  "))

if selectNum==1:
    yearInput = int(input("Year : "))

    fileMatrix = []
    with open('Error Rate.csv', 'r') as fileRead:
        csvFirst = csv.reader(fileRead)
        for i in csvFirst:
            fileMatrix.append(i)

    y_rate = []
    for i in range(len(fileMatrix[yearInput - 2001]) - 1):
        y_rate.append(float(fileMatrix[yearInput - 2001][i + 1]))

    x_country = ['AUS', 'BRA', 'UK', 'CAN', 'CHL', 'CZE', 'HUN', 'JPN', 'MEX', 'NZL', 'POL', 'RUS', 'KOR']

    N_of_groups = len(x_country)
    index = np.arange(N_of_groups)

    plt.bar(index, y_rate, tick_label=x_country, align='center')

    plt.xlabel('Country')
    plt.ylabel('Error Rate (%) ')
    plt.title('Error Rate in ' + str(yearInput))
    plt.xlim(-1, N_of_groups)
    plt.ylim(-100, 100)
    fig = plt.gcf()
    plt.show()

    bar_width = 0.2
    opacity = 0.5

    plt.bar(index, y_rate, bar_width, tick_label=x_country, align='center', alpha=opacity, color='b', label='year')
    fig.savefig('Chart_' + str(yearInput) + '.png')

elif selectNum == 2:
    countryInput = input("Country : ")
    countryNum = which_Country(countryInput)

    fileMatrix = []
    with open('Error Rate.csv', 'r') as fileRead:
        csvFirst = csv.reader(fileRead)
        for i in csvFirst:
            fileMatrix.append(i)

    y_rate = []
    for i in range(16):
        y_rate.append(float(fileMatrix[i][countryNum]))

    x_year = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15']

    N_of_groups = len(x_year)
    index = np.arange(N_of_groups)

    plt.bar(index, y_rate, tick_label=x_year, align='center')

    plt.xlabel('Year')
    plt.ylabel('Error Rate (%) ')
    plt.title('Error Rate of ' + countryInput + " (21st Century)")
    plt.xlim(-1, N_of_groups)
    plt.ylim(-100, 100)
    fig = plt.gcf()
    plt.show()

    bar_width = 0.2
    opacity = 0.5

    plt.bar(index, y_rate, bar_width, tick_label=x_year, align='center', alpha=opacity, color='#AA2848', label='rainfall')
    fig.savefig("Chart_" + countryInput + ".png")
else:
    print("error occured")

