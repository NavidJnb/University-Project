import random

a = []
for i in range(n):
    a += [random.random()]

a = [random.random() for i in range(n)]

for v in a:
    print(v)

maximum = a[0]
for v in a[1:]:
    if (v > maximum):
        maximum = v

maximum = max(a)

total = 0.0
for v in a:
    total += v
average = total / len(a)

b = []
for v in a:
    b += [v]

b = a[:]

n = len(a)
for i in range(n // 2):
    temp = a[i]
    a[i] = a[n - 1 - i]
    a[n - 1 - i] = temp

a = a[::-1]
