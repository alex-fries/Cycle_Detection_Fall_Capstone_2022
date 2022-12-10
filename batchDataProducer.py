import johnsonRunner
import sys
import threading

def runData(totalProcesses, totalResources, dirName = 'testCase'):
    for j in range(5):
        #totalProcesses = 18
        #totalResources = 18
        probabilityOfEdgeCreation = .3 + (.1 * (j))
        directoryToPutIn = dirName + str(j+1) + "/"

        for i in range(5000):
            johnsonRunner.main(i+1, totalProcesses, totalResources, probabilityOfEdgeCreation, directoryToPutIn)
        print("Job done")

t1 = threading.Thread(target = runData, args = (10, 10, '10_10_'))
t2 = threading.Thread(target = runData, args = (11, 11, '11_11_'))

t1.start()
t2.start()

t1.join()
print("done")
t2.join()
print("done")


t3 = threading.Thread(target = runData, args = (12, 12, '12_12_'))
t4 = threading.Thread(target = runData, args = (13, 13, '13_13_'))

t3.start()
t4.start()

t3.join()
print("fourteen seven")
t4.join()
print("sixteen eight done")

"""
t5 = threading.Thread(target = runData, args = (14, 14, 'eight_four_'))
t6 = threading.Thread(target = runData, args = (15, 15, 'six_three'))

t5.start()
t6.start()

t5.join()
print("eight four done")
t6.join()
print("six three done")


#now trying more resources than threads
t7 = threading.Thread(target = runData, args = (4, 8, 'four_eight_'))
t8 = threading.Thread(target = runData, args = (5, 10, 'five_ten_'))

t7.start()
t8.start()

t7.join()
print("four eight done")
t8.join()
print("five 10 done")



t9 = threading.Thread(target = runData, args = (6, 12, 'six_tweleve'))
t10 = threading.Thread(target = runData, args = (7, 14, 'six_three'))

t9.start()
t10.start()

t9.join()
print("six tweleve done")
t10.join()
print("six three done")


t11 = threading.Thread(target = runData, args = (3, 6, 'three_six_'))
t12 = threading.Thread(target = runData, args = (8, 16, 'eight_sixteen'))

t11.start()
t12.start()

t11.join()
print("three six done")
t12.join()
print("eight sixteen done")
"""


