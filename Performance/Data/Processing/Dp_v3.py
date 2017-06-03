import numpy as np
#import plotly.plotly as py
#import plotly.graph_objs as go
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter
import matplotlib.pyplot as plt
from matplotlib import pylab
from scipy.interpolate import UnivariateSpline
import csv

def readMyFile(filename):
    head_s = []
    flow_s = []
    flow = []
    head = []
    NPSH = []

    with open('17500.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvReader:
            head_s.append(row[0])
            flow_s.append(row[1])
            flow.append(row[2])
            head.append(row[3])
            NPSH.append(row[5])
    return np.array(head_s), np.array(flow_s), np.array(flow), np.array(head), np.array(NPSH)

head_s, flow_s, flow, head, NPSH = readMyFile("17500,csv")

head = np.delete(head, np.where(head == '')[0])
flow = np.delete(flow, np.where(flow == '')[0])
NPSH = np.delete(NPSH, np.where(NPSH == '')[0])

# Remove point beyond run-out
flow_adj = (flow[1:])
head_adj = (head[1:])

print(len(flow_s), len(head_s))
print(len(flow), len(head))
print(len(flow_adj), len(head_adj))
print(len(flow), len(NPSH))

# Trend lines
spl = UnivariateSpline(sorted(flow_adj), sorted(head_adj, reverse = True))
xs = np.linspace(3.5, 9.5, 1000)
spl.set_smoothing_factor(100)

# Plot Main
# plt.plot(flow_adj, head_adj, 'r--', flow_s, head_s, 'r--', ms=5)
plt.figure(figsize=(10, 6), dpi=80)
plt.plot(xs, spl(xs), 'k--', lw=2.5)
plt.plot(flow_s, head_s, 'k-', lw=2.5, label = 'System')
plt.plot(flow, NPSH, 'k-', lw=2.5, label = 'NPSHr')

#################################################################################
# Annotations

# plt.plot([8.96, 8.96], [0, 449.438], color='red', linewidth=2.5, linestyle="--")
plt.scatter([8.9612, ], 449.438, color='red', s = 100)
plt.annotate('BEP',
             xy=(8.96, 449.438), xycoords='data',
             xytext=(-80, 90), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))
plt.legend(loc='upper left')

plt.xlabel('Capacity [G.P.M.]', fontsize=16)
plt.ylabel('Head [ft]', fontsize=16)


#################################################################################

plt.axis([0, 12, 0, 1000])
plt.show()