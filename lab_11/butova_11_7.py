def a(x,n):
    xk = x
    for k in range(1, n+1):
        xk = (xk * x**2) / (2*k * (2*k + 1))
    return xk

def b(x, n):
    xk = -x
    for k in range(2, n+1):
        xk = xk * (-x * (k-1)/k)
    return xk

def c(x, n):
    xk = 1.0
    for k in range(1, n + 1):
        start = k ** 2 - k + 1
        end = k ** 2 + k
        factorial_gap = 1
        for i in range(start, end + 1):
            factorial_gap *= i
        xk = xk * (-x / factorial_gap)
    return xk

def d(x, n):
    xk = 1
    for k in range(1, n + 1):
        xk = (xk * (k+1) * x)/k**2
    return xk

print(a(2, 5))
print(b(2, 5))
print(c(2, 5))
print(d(2, 5))
