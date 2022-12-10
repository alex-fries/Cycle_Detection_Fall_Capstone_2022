"""
//NOTE THIS FILE IS CALLED aTestCaseDescription IN EVERY DIRECTORY
(vertex 0's connecting nodes)   4   5   8   9   0
.
.
.
vertex n's connecting nodes:    3   1   3
*
resource nodes:
1 2 3 ....
*
vertex removed: k
*
cycles before removal
*
cycles after removal
"""

import os
from pathlib import Path


def readAndParseDirectoryData(directory):
    listToAddToMainList = []

    print(directory)
    for dir2 in os.listdir(directory):
        #prints 'testCase1' ect
        totalCycles = 0
        totalCyclesAfterRemoval = 0
        totalCyclesRemoved = 0
        fileDescription = ''
        for file in os.listdir((os.path.join(directory, dir2))):
            #printing all the files in a given directory
            f = open(os.path.join((os.path.join(directory, dir2)), file))
            #print((os.path.join(directory, dir2)),file)

            if file != 'aTestCaseDescription.txt':
                fileData = f.readlines()
                #print(fileData)

                cyclesInFile = int(fileData[len(fileData)-3].strip())
                totalCycles += cyclesInFile

                cyclesInFileAfterRemoval = int(fileData[len(fileData)-1].strip())
                totalCyclesAfterRemoval += cyclesInFileAfterRemoval

                totalCyclesRemoved += (cyclesInFile - cyclesInFileAfterRemoval)

                #print(cyclesInFile, cyclesInFileAfterRemoval)
                #sys.exit(1)
            else:
                #print(file)
                #exit()
                for line in f:
                    fileDescription += line.strip() + " "

            f.close()
            #tempList2.append("Total cycles: " + str(totalCycles))
            #tempList2.append("Total cycles removed: " + str(totalCyclesRemoved))
            #tempList2.append("Total cycles left: " + str(totalCyclesAfterRemoval))
            #print(tempList2)
            #exit(1)
        directoryInfoList = []
        averageCyclesDetected = "Average cycles detected: " + str(totalCycles / 5000)
        averageCyclesAfterRemoval = "Average cycles left after removal: " + str(totalCyclesAfterRemoval / 5000)
        averageCyclesRemoved = "Average Cycles removed: " + str(totalCyclesRemoved / 5000)
        directoryLookedIn = fileDescription

        directoryInfoList.append(averageCyclesDetected)#keeping track of average in a single test case
        directoryInfoList.append(averageCyclesAfterRemoval)
        directoryInfoList.append(averageCyclesRemoved)
        directoryInfoList.append(directoryLookedIn)
        listToAddToMainList.append(directoryInfoList)

        print(directoryInfoList)

    dataBeingRead.append(listToAddToMainList)





rootDirectory = '/home/alex/Documents/Capstone/Programming/CapstoneControlData/'

dataBeingRead = []


for dir in os.listdir(rootDirectory):
    #through whole directory
    x_x_cases = os.path.join(rootDirectory, dir)
    readAndParseDirectoryData(x_x_cases)
    
fileToWriteTo = '/home/alex/Documents/Capstone/Programming/capstoneDataCompiled2.txt'
f = open(fileToWriteTo, 'w')
for lyst in dataBeingRead:
    for index in lyst:
        f.write('%s\n ' % index)
    f.write("\n")
f.close()

