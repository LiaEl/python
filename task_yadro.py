#!/usr/bin/env python3

import time

def decor(fn):
    def line(n):
        print('~' * 10, 'THESE NUMBERS ARE PRIME', '~' * 10)
        s_t = time.perf_counter()
        fn(n)
        t = time.perf_counter() - s_t
        print('~' * 6, 'PROCESSING TIME IS', t, '~' * 6)
    return line

@decor
def isPrime(n):
    arr = []
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            arr.append(i)

    print(arr[0], end='\t')
    for i in range(1, len(arr)):
        if i % 6 != 0:
            print(arr[i], end='\t')
        else:
            print()
            print(arr[i], end='\t')
    print()


isPrime(20)

