d = int(input())

c = []
for i in range(d):
    c.append(input().lower())

l = int(input())

s = []
for i in range(l):
    s += input().split()

for i in s:
    if i.lower() not in c:
        c.append(i.lower())
        print(i)
