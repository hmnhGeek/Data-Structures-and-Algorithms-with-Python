def reverse(l):
    L = []
    if len(l) == 0:
        return []

    else:
        return [l[-1]] + reverse(l[:-1])

print(reverse(['a', 'b', 'c', 'd', 'e']))
