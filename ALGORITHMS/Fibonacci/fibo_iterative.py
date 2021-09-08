def fibo(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        l = [0, 1]

        while len(l) != n:
            l.append(l[-1] + l[-2])
        
        return l

print(fibo(0))
print(fibo(1))
print(fibo(15))