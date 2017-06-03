import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

import matplotlib.pyplot as plt
from matplotlib import pylab
from scipy.interpolate import UnivariateSpline

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

head = np.delete(head, np.where(head == '')[0])
flow = np.delete(flow, np.where(flow == '')[0])

#flow_adj = flow[1:-(len(flow)-len(head))]
flow_adj = (flow[1:])
head_adj = (head[1:])

print(len(flow_s), len(head_s))
print(len(flow), len(head))
print(len(flow_adj), len(head_adj))

# Trend lines
spl = UnivariateSpline(sorted(flow_adj), sorted(head_adj, reverse = True))
xs = np.linspace(3, 9.5, 1000)
spl.set_smoothing_factor(1)
#plt.plot(xs, spl(xs), 'g', lw=2)

# Plot Main
#plt.plot(flow_adj, head_adj, 'r--', flow_s, head_s, 'r--', ms=5)

plt.plot(xs, spl(xs), 'g', flow_s, head_s, 'r--', ms=5)

plt.axis([0, 12, 0, 1000])
plt.show()
