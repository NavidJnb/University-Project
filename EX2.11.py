def f(x):
    return 5*x**4 + 3*x**2 + 2*x + 1

def df(x):
    return 20*x**3 + 6*x + 2

x = 1.0

for i in range(20):
    x = x - f(x) / df(x)

print(x)