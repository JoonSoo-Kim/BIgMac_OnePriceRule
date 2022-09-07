import csv


class myFile:
    def __init__(self, fileName=None, fileMode=None):
        self.fileMetrix = []
        if fileName == None and fileMode == None:
            print("need fileName and fileMode")
        elif fileName == None:
            print("need fileName")
        elif fileMode == None:
            print("need fileMode")

        fileRead = open(fileName, fileMode)
        if fileMode == 'r':
            csvFile = csv.reader(fileRead)
            for lineContent in csvFile:
                self.fileMatrix.append(lineContent)
            self.fileMatrix = self.fileMatrix[1:]
            self.fileMatrix.sort()

    def getStatus(self):
        if self.fileMatrix == None:
            print("Error occured")
            return False
        else:
            return True

    def getBody(self):
        if self.fileMatrix == None:
            print("Error occured")
            return False
        else:
            return self.fileMatrix[1:]

    def setContentHead(self, givenrList=None):
        if self.givenList == None:
            print("Error occured")
            return False
        else:
            self.headerList = self.givenList
            return True

    def setContentBody(self, givenList=None):
        if self.givenList == None:
            print("Error occured")
            return False
        else:
            self.bodyList = self.givenList
            return True

    def writefile(self):
        if self.getStatus() == False:
            print("Error occured")
            return False
        else:
            self.writeContent = self.headerList + self.bodyList
            mywriter = csv.writer(fileRead)
            for i in range(len(self.writeContent)):
                csvWrite.writerow(self.writeContent[i])
            return True

    def closefile(self):
        if getStatus()==False:
            print("Error occured")
        else:
            fileRead.close()
            return True



def mergeList(list1,list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            if list1[i][0]==list2[j][0]:
                scoreSum=0
                list1[i].extend(list2[j][1:])
                scoreSum = int(list2[j][1])+int(list2[j][2])+int(list2[j][3])
                average = scoreSum//3
                list1[i].extend([str(average)])
    print(list1)
    return list1



