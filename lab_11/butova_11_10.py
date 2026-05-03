def A(n):
    f = 4 * n + 2
    for i in range(n - 1, -1, -1):
        print(f)
        f = (4 * i + 2) + 1 / f
    return f

print(A(5))