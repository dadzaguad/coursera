from math import sqrt


def MinDivisor(n):
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return i
        i += 1
    return n


n = int(input())
print(MinDivisor(n))
