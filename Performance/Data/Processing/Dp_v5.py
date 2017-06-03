import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import csv
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

def readMyFile(filename):
    head_s = []
    flow_s = []
    flow = []
    head = []
    NPSH = []
    effic = []

    with open('17500.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvReader:
            head_s.append(row[0])
            flow_s.append(row[1])
            flow.append(row[2])
            head.append(row[3])
            NPSH.append(row[5])
            effic.append(row[6])
    return np.array(head_s), np.array(flow_s), np.array(flow), np.array(head), np.array(NPSH), np.array(effic)

head_s, flow_s, flow, head, NPSH, effic = readMyFile("17500,csv")

head = np.delete(head, np.where(head == '')[0])
flow = np.delete(flow, np.where(flow == '')[0])
NPSH = np.delete(NPSH, np.where(NPSH == '')[0])
effic = np.delete(NPSH, np.where(NPSH == '')[0])

# Remove point beyond run-out
flow_adj = (flow[1:])
head_adj = (head[1:])

print(len(flow_s), len(head_s))
print(len(flow), len(head))
print(len(flow_adj), len(head_adj))
print(len(flow), len(NPSH))

#################################################################################

# Trend lines
spl = UnivariateSpline(sorted(flow_adj), sorted(head_adj, reverse = True))
xs = np.linspace(3.5, 9.5, 1000)
spl.set_smoothing_factor(100)

#################################################################################

host = host_subplot(111, axes_class=AA.Axes)
host.patch.set_facecolor('white')
plt.subplots_adjust(right=0.75)

# par1 = host.twinx()
par2 = host.twinx()
par3 = host.twinx()

offset = 30
new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(offset, 0))
par2.axis["right"].toggle(all=True)



host.set_xlim(0, 12)
host.set_ylim(0, 1000)


host.set_xlabel('Capacity [G.P.M.]', fontsize=16)
host.set_ylabel('Head [ft]', fontsize=16)
# par1.set_ylabel('NPSHr [ft]', fontsize=16)
par2.set_ylabel('NPSHr [ft]', fontsize=16)

p1, = host.plot(xs, spl(xs), 'g-', lw=2.5, label="EFS Pump")
p2, = host.plot(flow_s, head_s, 'k-', lw=2.5, label = 'System')
p3, = par2.plot(flow, NPSH, 'b-', lw=2.5, label = 'NPSH')

# par1.set_ylim(0, 1000)
par2.set_ylim(30, 70)

host.legend()

# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())


#################################################################################
# Annotations

# plt.plot([8.96, 8.96], [0, 449.438], color='red', linewidth=2.5, linestyle="--")
plt.scatter([8.9612, ], 449.438, color='red', s = 75)
plt.scatter([3.5, ], 626, color='red', s = 50)
plt.scatter([9.5, ], 409, color='red', s = 50)
plt.annotate('BEP',
             xy=(8.96, 449.438), xycoords='data',
             xytext=(-60, 80), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1"))



#################################################################################


plt.draw()
plt.show()