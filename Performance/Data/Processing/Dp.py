import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import csv

def readMyFile(filename):
    head_s = []
    flow_s = []
    flow = []
    head = []

    with open('17500.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvReader:
            head_s.append(row[0])
            flow_s.append(row[1])
            flow.append(row[2])
            head.append(row[3])
    return np.array(head_s), np.array(flow_s), np.array(flow), np.array(head)

head_s, flow_s, flow, head = readMyFile("17500,csv")
print(head)

head = np.delete(head, np.where(head == '')[0])
print(len(flow_s), len(head_s))
print(head)
#print(len(flow), len(head))

plt.plot(flow[1:-(len(flow)-len(head))], head[1:], 'b--', flow_s, head_s, 'r--')
plt.plot(flow_s, head_s, 'b--')
plt.axis([0, 12, 0, 1000])
plt.show()
