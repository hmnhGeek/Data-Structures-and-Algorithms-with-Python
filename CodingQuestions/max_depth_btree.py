
def get_levels(l):
    L = []
    i = 0

    while i < len(l):
        L.append(l[i : i*2 + 1])
        i = i*2 + 1

    return L

def max_depth(inorder):
    levels = get_levels(inorder)
    depth = len(levels)
    return depth

l = [3,9,20, None, None, 15, 7]
print(max_depth(l))
print(max_depth([1, None, 2]))
print(max_depth([]))
print(max_depth([0]))