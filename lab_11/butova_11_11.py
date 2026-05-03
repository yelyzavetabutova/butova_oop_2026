def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0: return False
    return True

def fib(n):
    a, b = 0, 1
    for i in range(1, n + 1):
        f = b
        if is_prime(f):
            is_valid = is_prime(i) or i == 4
            print("n =", i, "Fn =", f, ":", is_valid)
        a, b = b, a + b