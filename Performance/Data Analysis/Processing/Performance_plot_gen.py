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
    npsh = []
    effic = []

    with open('17500_temp.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in csvReader:
            head_s.append(row[0])
            flow_s.append(row[1])
            flow.append(row[2])
            head.append(row[3])
            npsh.append(row[5])
            effic.append(row[6])
    return np.array(head_s), np.array(flow_s), np.array(flow), np.array(head), np.array(npsh), np.array(effic)

head_s, flow_s, flow, head, npsh, effic = readMyFile("17500,csv")

head = np.delete(head, np.where(head == '')[0])
flow = np.delete(flow, np.where(flow == '')[0])
npsh = np.delete(npsh, np.where(npsh == '')[0])
effic = np.delete(effic, np.where(effic == '')[0])

# Remove point beyond run-out
flow_s_adj = (flow_s[2:])
head_s_adj = (head_s[2:])
flow_adj = (flow[1:])
head_adj = (head[1:])
effic_adj = (effic[1:])
#effic_adj = effic
npsh_adj = (npsh[1:])

print(len(flow_s), len(head_s))
print(len(flow), len(head))
print(len(flow_adj), len(head_adj))

#################################################################################

# Trend lines

sp4 = UnivariateSpline(flow_adj, sorted(head_adj, reverse = False))
xs4 = np.linspace(3.75, 10.5, 1000)
sp4.set_smoothing_factor(1000)

sp2 = UnivariateSpline(sorted(flow_adj), effic_adj)
xs2 = np.linspace(3.75, 10.5, 1000)
sp2.set_smoothing_factor(1000)

sp3 = UnivariateSpline(sorted(flow_adj), sorted(npsh_adj, reverse = True))
xs3 = np.linspace(3.75, 10.5, 1000)
sp3.set_smoothing_factor(100)

#################################################################################
params = {'axes.labelsize': 32,'axes.titlesize':1, 'font.size': 20, 'legend.fontsize': 24,
          'xtick.labelsize': 28, 'ytick.labelsize': 28, 'legend.frameon': False}
plt.rcParams.update(params)



host = host_subplot(111, axes_class=AA.Axes)
host.patch.set_facecolor('white')
plt.subplots_adjust(right=0.75)

# par1 = host.twinx()
par2 = host.twinx()
par3 = host.twinx()

new_fixed_axis = par2.get_grid_helper().new_fixed_axis
par2.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par2,
                                    offset=(30, 0))
par2.axis["right"].toggle(all=True)

offset = 30
new_fixed_axis = par3.get_grid_helper().new_fixed_axis
par3.axis["right"] = new_fixed_axis(loc="right",
                                    axes=par3,
                                    offset=(120, 0))
par3.axis["right"].toggle(all=True)

host.set_xlim(2, 12)
host.set_ylim(0, 800)

host.set_xlabel('Capacity [G.P.M.]', labelpad=100)
host.set_ylabel('Head [ft]', labelpad=100)
# par1.set_ylabel('NPSHr [ft]')
par2.set_ylabel('NPSH [ft]')
par3.set_ylabel('Efficiency %')

p1, = host.plot(xs4, sp4(xs4), 'g-', lw=3, label= 'EFS Pump')
p2, = host.plot(flow_s_adj, head_s_adj, 'k-', lw=3, label = 'System Curve')
p3, = par2.plot(xs3, sp3(xs3), 'b-', lw=3, label = 'NPSH')
p4, = par3.plot(xs2, sp2(xs2), 'r-', lw=3, label = 'Efficiency')

# par1.set_ylim(0, 1000)
par2.set_ylim(20, 60)
par3.set_ylim(0, 100)

host.legend()

# host.axis["left"].label.set_color(p1.get_color())
# par1.axis["right"].label.set_color(p2.get_color())
par2.axis["right"].label.set_color(p3.get_color())
par3.axis["right"].label.set_color(p4.get_color())

#################################################################################
#Annotations

plt.plot([9.362, 9.362], [0, 750], color='black', linewidth=2.5, linestyle="--")
plt.scatter([9.36, ], 533, color='red', s = 110)
#plt.scatter([8.97, ], 232.97, color='red', s = 90)
#plt.scatter([8.97, ], 96, color='red', s = 90)
#plt.scatter([3.74, ], 665, color='black', s = 90)
plt.scatter([10.5, ], 477, color='black', s = 90)

# Point Moarkers
plt.annotate('Best Operating Point',
             xy=(9.362, 650), xycoords='data',
             xytext=(-300, 50), textcoords='offset points', fontsize=22,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.1", linewidth=2))
plt.annotate('Run-Out',
             xy=(10.5, 477), xycoords='data',
             xytext=(25, 75), textcoords='offset points', fontsize=22,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.07", linewidth=2))
plt.annotate('Shut-Off Head',
             xy=(3.74, 593), xycoords='data',
             xytext=(25, 75), textcoords='offset points', fontsize=22,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.07", linewidth=2))

#################################################################################

plt.draw()
plt.show()