import sys

l = []

d = {}
for i in range(1, 12):
    d[i] = [0, 0]

with open(sys.argv[1]) as fi:
    for line in fi:
        b = line.strip().split()
        d[int(b[0])][0] += float(b[2])
        d[int(b[0])][1] += 1

for i in d.keys():
    if d[i][1] == 0:
        print(i, '-')
    else:
        print(i, d[i][0] / d[i][1])
