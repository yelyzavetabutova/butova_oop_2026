def a(n):
    t0, t1, t2, t3, t4 = 1, 1, 1, 2, 2
    if n < 5:
        return [t0, t1, t2, t3, t4][n]
    for _ in range(n - 4):
        t5 = t4 + t0
        t0, t1, t2, t3, t4 = t1, t2, t3, t4, t5
    return t4

def b(n):
    t0 = 1
    t1 = 1
    t2 = 1
    t3 = 2
    t4 = 2
    t5 = 3
    t6 = 4
    t7 = 5
    for _ in range(n - 7):
        t8 = t6 + t4 + t0
        t0 = t1
        t1 = t2
        t2 = t3
        t3 = t4
        t4 = t5
        t5 = t6
        t6 = t7
        t7 = t8
    return t7

def c(n):
    t0 = 1
    t1 = 1
    t2 = 1
    t3 = 2
    t4 = 2
    t5 = 3
    t6 = 4
    for _ in range(n - 6):
        t7 = 2 * t5 - t0
        t0 = t1
        t1 = t2
        t2 = t3
        t3 = t4
        t4 = t5
        t5 = t6
        t6 = t7
    return t6

def d(n):
    t0, t1, t2 = 1, 1, 1
    t3, t4, t5 = 2, 2, 3
    t6, t7, t8 = 4, 5, 7
    t9, t10, t11 = 9, 12, 16
    t12, t13 = 21, 28
    for _ in range(n - 13):
        t14 = 4 * t9 + t0
        t0 = t1
        t1 = t2
        t2 = t3
        t3 = t4
        t4 = t5
        t5 = t6
        t6 = t7
        t7 = t8
        t8 = t9
        t9 = t10
        t10 = t11
        t11 = t12
        t12 = t13
        t13 = t14
    return t13

print(a(20))
print(b(20))
print(c(20))
print(d(20))