def segregate(l):
    even, odd = 0, len(l) - 1

    while even < odd:
        if l[even] % 2 == 0: even += 1
        else:
            l[even], l[odd] = l[odd], l[even]
            odd -= 1
    
    return l

l = [6, 3, 10, 15, 17, 2]
print(segregate(l))