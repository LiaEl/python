a = [i for i in input()]
b = [i for i in input()]

d1 = {}
d2 = {}

for i in range(len(a)):
    for i in range(len(b)):
        d1[a[i]] = b[i]
        d2[b[i]] = a[i]

c1 = [d1[i] for i in input()]
c2 = [d2[i] for i in input()]

k1, k2 = '', ''
for i in range(len(c1) - 1):
    k1 += c1[i]
    k2 += c2[i]
print(str(k1) + str(c1[i+1]))
print(str(k2) + str(c2[i+1]))
