import os
import sys

class Logger(object):
    def __init__(self):
        log_dir = f'my_yq_out_03.txt'
        self.terminal = sys.stdout
        self.log = open(log_dir, 'a')
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout = Logger()

filename = None
if len(sys.argv) > 1:
    filename = sys.argv[1]
if filename is None:
    print("Error: Input file not specified!")

with open(filename, 'r') as f:
    dic = {}
    for line in f.readlines():
        lis = line.split()
        province, city, num = lis[0], lis[1], lis[2]
        if num != '0':
            if province not in dic:
                dic[province] = []
                dic[province].append([city, num])
            else:
                dic[province].append([city, num])

for prov in dic.keys():
    print(prov)
    for item in dic[prov]:
        city, num = item[0], item[1]
        print(f'{city}\t{num}')
    print()
