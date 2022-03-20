import os
import sys

in_dir = None
out_dir = None
PROV = None
if len(sys.argv) == 3:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
else:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
    PROV = sys.argv[3]

class Logger(object):
    def __init__(self):
        log_dir = out_dir
        self.terminal = sys.stdout
        self.log = open(log_dir, 'w')
    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
    def flush(self):
        pass
sys.stdout = Logger()


with open(in_dir, 'r') as f:
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

if PROV is None:
    for prov in dic.keys():
        print(prov)
        for item in dic[prov]:
            city, num = item[0], item[1]
            print(f'{city}\t{num}')
        print()
else:
    print(PROV)
    for item in dic[PROV]:
        city, num = item[0], item[1]
        print(f'{city}\t{num}')
    print()
