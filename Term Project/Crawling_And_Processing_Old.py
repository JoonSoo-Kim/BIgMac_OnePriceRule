import pandas as pd
import csv


# Crawling Start

#2000
data_file_2000 = pd.read_html('http://bigmacindex.org/2000-big-mac-index.html', flavor='html5lib')
data_file=data_file_2000[0]

data_file.to_csv("2000.csv", mode='w', header=False)

#2001
data_file_2001 = pd.read_html('http://bigmacindex.org/2001-big-mac-index.html', flavor='html5lib')
data_file=data_file_2001[0]

data_file.to_csv("2001.csv", mode='w', header=False)

#2002
data_file_2002 = pd.read_html('http://bigmacindex.org/2002-big-mac-index.html', flavor='html5lib')
data_file=data_file_2002[0]

data_file.to_csv("2002.csv", mode='w', header=False)

#2003
data_file_2003 = pd.read_html('http://bigmacindex.org/2003-big-mac-index.html', flavor='html5lib')
data_file=data_file_2003[0]

data_file.to_csv("2003.csv", mode='w', header=False)

#2004
data_file_2004 = pd.read_html('http://bigmacindex.org/2004-big-mac-index.html', flavor='html5lib')
data_file=data_file_2004[0]

data_file.to_csv("2004.csv", mode='w', header=False)

#2005
data_file_2005 = pd.read_html('http://bigmacindex.org/2005-big-mac-index.html', flavor='html5lib')
data_file=data_file_2005[0]

data_file.to_csv("2005.csv", mode='w', header=False)

#2006
data_file_2006 = pd.read_html('http://bigmacindex.org/2006-big-mac-index.html', flavor='html5lib')
data_file=data_file_2006[0]

data_file.to_csv("2006.csv", mode='w', header=False)

#2007
data_file_2007 = pd.read_html('http://bigmacindex.org/2007-big-mac-index.html', flavor='html5lib')
data_file=data_file_2007[0]

data_file.to_csv("2007.csv", mode='w', header=False)

#2008
data_file_2008 = pd.read_html('http://bigmacindex.org/2008-big-mac-index.html', flavor='html5lib')
data_file=data_file_2008[0]

data_file.to_csv("2008.csv", mode='w', header=False)

#2009
data_file_2009 = pd.read_html('http://bigmacindex.org/2009-big-mac-index.html', flavor='html5lib')
data_file=data_file_2009[0]

data_file.to_csv("2009.csv", mode='w', header=False)

#2010
data_file_2010 = pd.read_html('http://bigmacindex.org/2010-big-mac-index.html', flavor='html5lib')
data_file=data_file_2010[0]

data_file.to_csv("2010.csv", mode='w', header=False)

#2011
data_file_2011 = pd.read_html('http://bigmacindex.org/2011-big-mac-index.html', flavor='html5lib')
data_file=data_file_2011[0]

data_file.to_csv("2011.csv", mode='w', header=False)

#2012
data_file_2012 = pd.read_html('http://bigmacindex.org/2012-big-mac-index.html', flavor='html5lib')
data_file=data_file_2012[0]

data_file.to_csv("2012.csv", mode='w', header=False)

#2013
data_file_2013 = pd.read_html('http://bigmacindex.org/2013-big-mac-index.html', flavor='html5lib')
data_file=data_file_2013[0]

data_file.to_csv("2013.csv", mode='w', header=False)

#2014
data_file_2014 = pd.read_html('http://bigmacindex.org/2014-big-mac-index.html', flavor='html5lib')
data_file=data_file_2014[0]

data_file.to_csv("2014.csv", mode='w', header=False)

#2015
data_file_2015 = pd.read_html('http://bigmacindex.org/2015-big-mac-index.html', flavor='html5lib')
data_file=data_file_2015[0]

data_file.to_csv("2015.csv", mode='w', header=False)

# Crawling End

# Processing Start
wanted_country = ['Australia', 'Brazil', 'Canada', 'Chile', 'Czech Republic', 'Hungary', 'Japan', 'South Korea', 'Mexico', 'New Zealand', 'Russia', 'Poland', 'Britain', 'United States']

#2000
fileMatrix = []
fileMatrix_2=[]

with open("2000.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2000_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2001
fileMatrix = []
fileMatrix_2=[]

with open("2001.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2001_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2002
fileMatrix = []
fileMatrix_2=[]

with open("2002.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2002_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2003
fileMatrix = []
fileMatrix_2=[]

with open("2003.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2003_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2004
fileMatrix = []
fileMatrix_2=[]

with open("2004.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2004_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2005
fileMatrix = []
fileMatrix_2=[]

with open("2005.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2005_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2006
fileMatrix = []
fileMatrix_2=[]

with open("2006.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2006_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2007
fileMatrix = []
fileMatrix_2=[]

with open("2007.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2007_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2008
fileMatrix = []
fileMatrix_2=[]

with open("2008.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2008_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2009
fileMatrix = []
fileMatrix_2=[]

with open("2009.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2009_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2010
fileMatrix = []
fileMatrix_2=[]

with open("2010.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2010_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2011
fileMatrix = []
fileMatrix_2=[]

with open("2011.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2011_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2012
fileMatrix = []
fileMatrix_2=[]

with open("2012.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2012_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2013
fileMatrix = []
fileMatrix_2=[]

with open("2013.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2013_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2014
fileMatrix = []
fileMatrix_2=[]

with open("2014.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2014_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

#2015
fileMatrix = []
fileMatrix_2=[]

with open("2015.csv", 'r') as fileRead:

    csvFirst = csv.reader(fileRead)

    for lineContent in csvFirst:
        fileMatrix.append(lineContent)

    for i in range(len(fileMatrix)):
        fileMatrix[i]=fileMatrix[i][1:4]
        if fileMatrix[i][0] in wanted_country:
            fileMatrix_2.append(fileMatrix[i])

with open("2015_P.csv", 'w', newline='') as fileWrite:

    csvSecond=csv.writer(fileWrite)

    for i in range(len(fileMatrix_2)):
        csvSecond.writerow(fileMatrix_2[i])

# Processing End