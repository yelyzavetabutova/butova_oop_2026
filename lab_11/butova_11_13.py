def detA(n):
    a1 = 2
    a2 = 3
    for _ in range(n - 2):
        a3 = 2 * a2 - a1
        a1 = a2
        a2 = a3
    return a2

def detB(n):
    a1 = 3
    a2 = 7
    for _ in range(n - 2):
        a3 = 3 * a2 - 2 * a1
        a1 = a2
        a2 = a3
    return a2

print(detA(5))
print(detB(5))