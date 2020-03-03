from os import getcwd, listdir
from os.path import isfile, join

csv_header1 = ',/intelcpu/0/load/1,/intelcpu/0/load/2,/intelcpu/0/load/3,/intelcpu/0/load/4,/intelcpu/0/load/0,/intelcpu/0/temperature/0,/intelcpu/0/temperature/1,/intelcpu/0/temperature/2,/intelcpu/0/temperature/3,/intelcpu/0/temperature/4,/intelcpu/0/clock/1,/intelcpu/0/clock/2,/intelcpu/0/clock/3,/intelcpu/0/clock/4,/intelcpu/0/power/0,/intelcpu/0/power/1,/intelcpu/0/power/2,/intelcpu/0/power/3,/intelcpu/0/clock/0,/ram/load/0,/ram/data/0,/ram/data/1,/hdd/0/temperature/0,/hdd/0/load/0'
csv_header2 = 'Time,"CPU Core #1","CPU Core #2","CPU Core #3","CPU Core #4","CPU Total","CPU Core #1","CPU Core #2","CPU Core #3","CPU Core #4","CPU Package","CPU Core #1","CPU Core #2","CPU Core #3","CPU Core #4","CPU Package","CPU Cores","CPU Graphics","CPU DRAM","Bus Speed","Memory","Used Memory","Available Memory","Temperature","Used Space"'
csv_out = 'merged.csv'

path = getcwd()

csv_list = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.csv') and f != 'merged.csv']

csv_merge = open(csv_out, 'w')
csv_merge.write(csv_header2)
csv_merge.write('\n')

for file in csv_list:
    print(file)
    csv_in = open(file)
    for line in csv_in:
        if line.startswith(csv_header1) or line.startswith(csv_header2):
            continue
        csv_merge.write(line)
    csv_in.close()
csv_merge.close()
print('Verify consolidated CSV file : ' + csv_out)