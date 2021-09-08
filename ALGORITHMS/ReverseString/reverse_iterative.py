def reverse(l):
    up = len(l) -1
    L = []

    while up != -1:
        L.append(l[up])
        up -= 1
    
    return L 

print(reverse(['a', 'b', 'c', 'd', 'e']))