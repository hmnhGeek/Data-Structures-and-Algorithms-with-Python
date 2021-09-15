calculations = 0

def memo():
    cache = {}

    def fibo(n):
        global calculations
        calculations += 1
        if n in cache: return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = fibo(n-1) + fibo(n-2)
                return cache[n]

    return fibo

f = memo()
print(f(100))
print("Total calculations = ", calculations)