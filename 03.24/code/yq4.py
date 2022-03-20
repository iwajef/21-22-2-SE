import os
import sys

in_dir = None
out_dir = None
PROV = None
if len(sys.argv) == 3:
    in_dir = sys.argv[1]
    out_dir = sys.argv[2]
elif len(sys.argv) == 4:
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

new_key_dic = {}
for prov in dic.keys():
    prov_total_sum = 0
    for item in dic[prov]:
        prov_total_sum += int(item[1])
    new_key = (prov, prov_total_sum)
    new_key_dic[prov] = new_key

new_dict = dict((new_key_dic[old_key], value) for (old_key, value) in dic.items())


if PROV is None:
    for prov in sorted(new_dict.keys(), key=lambda x: x[1], reverse=True):
        print(f'{prov[0]}\t{prov[1]}')
        sorted_cities = sorted(new_dict[prov], key=lambda x: int(x[1]), reverse=True)
        for item in sorted_cities:
            city, num = item[0], item[1]
            print(f'{city}\t{num}')
        print()
else:
    print(PROV)
    sorted_cities = sorted(dic[PROV], key=lambda x: int(x[1]), reverse=True)
    for item in sorted_cities:
        city, num = item[0], item[1]
        print(f'{city}\t{num}')
    print()
