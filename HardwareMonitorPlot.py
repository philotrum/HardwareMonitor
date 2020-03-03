#!/user/bin/env python

from pandas import DataFrame, read_csv
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

col_names = ['Time','CPU_LoadCore#1','CPU_LoadCore#2','CPU_LoadCore#3','CPU_LoadCore#4','CPU_Total','CPU_TempCore#1','CPU_TempCore#2','CPU_TempCore#3','CPU_TempCore#4','CPU_TempPackage','CPU_ClockCore#1','CPU_ClockCore#2','CPU_ClockCore#3','CPU_ClockCore#4','CPU_PowerPackage','CPU_PowerCores','CPU_PowerGraphics','CPU_PowerDRAM','Clock_BusSpeed','Memory','UsedMemory','AvailableMemory','Temperature','UsedSpace']

df = pd.read_csv('merged.csv', header=0, names=col_names)

df['Time'] = pd.to_datetime(df.Time, format='%m/%d/%Y %H:%M:%S')

Fig = plt.figure('Computer Information_Darwin')
Fig.subplots_adjust(hspace=0.1)
Fig.suptitle('Computer resources\nDarwin', fontsize=14, fontweight='bold')


Ax1 = Fig.add_subplot(311)
Ax1.plot(df.Time, df.UsedMemory)
Ax1.set_ylabel('Memory usage\nGb')
Ax1.grid(True)
Ax1.set_ylim(0, 8)
Ax1.get_yaxis().get_major_formatter().set_useOffset(False)

Ax2 =Fig.add_subplot(312, sharex=Ax1)
Ax2.plot(df.Time, df.CPU_Total)
Ax2.set_ylabel('CPU usage\n%')
Ax2.grid(True)
Ax2.set_ylim(0, 100)
Ax2.get_yaxis().get_major_formatter().set_useOffset(False)

Ax3 =Fig.add_subplot(313, sharex=Ax1)
Ax3.plot(df.Time, df.UsedSpace)
Ax3.set_ylabel('Hdd Usage\n%')
Ax3.grid(True)
Ax3.set_ylim(0, 100)
Ax3.get_yaxis().get_major_formatter().set_useOffset(False)

Fig.autofmt_xdate()
plt.show()