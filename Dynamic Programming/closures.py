def addto5():
    cache = {}

    def add(n):
        if n not in cache:
            print("First execution...")
            cache[n] = n + 5
        
        return cache[n]

    return add

memoized = addto5()
print(memoized(5))
print(memoized(5))