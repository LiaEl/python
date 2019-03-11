c = int(input())

m = [0, 0]

for i in range(c):
    s = input().split()
    if s[0] == 'север':
        m[1] += int(s[1])
    if s[0] == 'юг':
        m[1] -= int(s[1])
    if s[0] == 'запад':
        m[0] -= int(s[1])
    if s[0] == 'восток':
        m[0] += int(s[1])

print(m[0], m[1])
