import argparse
from prettytable import PrettyTable

parser = argparse.ArgumentParser(usage="-h for full usage")
parser.add_argument('size', help='table size')
args = parser.parse_args()
n = int(args.size)
m = list(list(range(1*i,(n+1)*i, i)) for i in range(1,n+1))
max_width = len(str(m[-1][-1])) + 1
for i in m:
    i = [str(j).rjust(max_width) for j in i]
    print ''.join(i)
