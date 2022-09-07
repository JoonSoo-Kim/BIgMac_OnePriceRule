import csv

class myFile():
    def __init__(self,fileName=None,openMode=None):
        self.fileName=fileName
        self.openMode=openMode
        if self.openMode == 'r' or self.openMode=='r+':
            self.status=True
            self.file=open(self.fileName,self.openMode)
            lines=csv.reader(self.file)
            self.memberList=[]
            for line in lines:
                self.memberList.append(line)
            mySort(self.memberList,0)
            print(self.memberList)
        elif self.openMode == 'w'or self.openMode=='w+':
            self.status=True
            self.file=open(self.fileName,self.openMode,newline='')
        else:
            self.status=False
            print('Open mode error')
    def getStatus(self):
        if not self.status:
            print("Opening file error")
        return self.status
    def getBody(self):
        if self.status:
            self.body=self.memberList[:len(self.memberList)-1]
            return self.body
        else:
            print('No file')
        return
    def setContentHead(self, head=None):
        if head is None:
            print('No head')
            return False
        else:
            self.writeHead=head
            return True
    def setContentBody(self,body=None):
        if body is None:
            print('No body')
            return False
        else:
            self.writeBody=body
            return True
    def writeFile(self):
        csvWriter=csv.writer(self.file)
        csvWriter.writerow(self.writeHead)
        for row in self.writeBody:
            csvWriter.writerow(row)
        return
    def closeFile(self):
        if self.status:
            self.file.close()
            return True
        else:
            print('No file')
            return False
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


def mySort(matrix,idx):
    for i in range(0,len(matrix)):
        for j in range(i,len(matrix)):
            if matrix[i][idx]>matrix[j][idx]:
                temp=matrix[i]
                matrix[i]=matrix[j]
                matrix[j]=temp

file1 = myFile("inputdata1.csv", 'r')
file2 = myFile("inputdata2.csv", 'r')

if (file1.getStatus() != False) and (file2.getStatus() != False):
    newList = mergeList(file1.getBody(), file2.getBody())

    file3 = myFile("output.csv", 'w')
    file3.setContentHead(["ID", "Name", "Course 1", "Course 2", "Course 3", "Average"])
    file3.setContentBody(newList)
    file3.writeFile()
    file3.closeFile()
else:
    print("input file error")

file1.closeFile()
file2.closeFile()