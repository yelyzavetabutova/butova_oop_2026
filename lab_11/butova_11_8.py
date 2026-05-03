def a(n):
    s = 0
    sign = 1
    for k in range(1, n+1):
        s = s + sign * k
        sign = -sign
    return s

def b(n):
    s = 0
    for k in range(1, n):
        a = 1 / (k * (k + 1))
        s = s + a
    return s

def c(n):
    s = 0
    for k in range(2, n + 1):
        sign = (-1)**k
        a = sign * (k - 1) / k
        s = s + a
    return s

print(a(5))
print(b(5))
print(c(5))