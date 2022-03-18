def dnf_sort(l):
    low, mid, high = 0, 0, len(l) - 1

    while mid < high:
        if l[mid] == 0:
            l[mid], l[low] = l[low], l[mid]
            low += 1
            mid += 1
        elif l[mid] == 1:
            mid += 1
        elif l[mid] == 2:
            l[mid], l[high] = l[high], l[mid]
            high -= 1
    
    return l

l = [0,1,2,0,2,1]
print(dnf_sort(l))