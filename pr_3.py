#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

n = 13195

factors = []

def isPrime(n):
    arr = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)

isPrime(n)

#
#for i in range(2, x):
#    if x % i == 0:
#        print(i)
#        factors.append(i)
#print('well done');
#
#for i in factors:
#        isPrime(i)
#        print(arr)
#
