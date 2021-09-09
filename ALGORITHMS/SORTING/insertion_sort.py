def insert_properly(l, data):
    # Given a sorted list l, insert data at its correct place.

    for i in range(len(l)):
        if data < l[i]:
            l.insert(i, data)
            return l
    
    l.append(data)
    return l

def insertion_sort(l):
    # we assume that the first item is at correct place, & so we start the loop
    # from index i = 1.

    for i in range(1, len(l)):
        l = insert_properly(l[0:i], l[i]) + l[i+1:]

        ## Insert l[i] in the sorted array before it, and prepend the result
        ## to the sub array after l[i]
    
    return l

l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
l = insertion_sort(l)
print(l)