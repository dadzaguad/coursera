h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
h1 = 3600 * h1
m1 = 60 * m1
h2 = 3600 * h2
m2 = 60 * m2
print((h2 + m2 + s2) - (h1 + m1 + s1))