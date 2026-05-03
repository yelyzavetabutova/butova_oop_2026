def a(n):
    p = 1
    for i in range(2, n+1):
        p = p * (1 - 1/i**2)
    return p

def b(n):
    p = 1
    f = 1
    for i in range(1, n + 1):
        f = f * i
        p = p * (2 + 1/f)
    return p

print(a(5))
print(b(5))