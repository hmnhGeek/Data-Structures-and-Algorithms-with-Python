def merge(tup):
    L = []
    for elem in tup:
        if type(elem) == type(1):
            L.append(elem)
        else:
            L += merge(elem)
    
    return L

def quick_sort(l):
    if len(l) == 0 or len(l) == 1:
        return l

    else:
        left, right = [], []
        pivot = -1

        # partition the elements based on pivot
        for i in range(len(l)-1):
            if l[i] < l[pivot]:
                left.append(l[i])
            else:
                right.insert(0, l[i])

        # if left or right or both are [] or [some_integer], then merge the three
        # eg. [2], [10 (pivot)], [] --> [2, 10]
        # eg. [], [10], [11] --> [10, 11]
        # eg. [], [10], [] --> [10]
        # eg. [1], [10], [11] --> [1, 10, 11]

        if len(left) <= 1 and len(right) <= 1:
            return left + [l[pivot]] + right

        # else recursively do for left and right and call merge
        else:
            subleft = quick_sort(left)
            subright = quick_sort(right)
            return merge((subleft, [l[pivot]], subright))

l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
l = quick_sort(l)
print(l)