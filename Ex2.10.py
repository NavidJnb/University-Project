def f(x):
    return x**2 -2

def df(x):
    return 2*x

t = 1.0

for i in range(10):
    t = t - f(t) / df(t)
    print(t)