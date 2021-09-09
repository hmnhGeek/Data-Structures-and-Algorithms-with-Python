def selection_sort(l):
    if l == []:
        return l

    else:
        MIN = 0

        for i in range(len(l)+1):
            for j in range(i+1, len(l)):
                if l[j] < l[MIN]:
                    MIN = j

            l.insert(i, l.pop(MIN))
        return l   

l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
l = selection_sort(l)

print(l)