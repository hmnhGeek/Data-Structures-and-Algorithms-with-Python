def merge(left, right):

    result = []
    leftIndex, rightIndex = 0, 0

    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex += 1
        else:
            result.append(right[rightIndex])
            rightIndex += 1
    
    return result + left[leftIndex:] + right[rightIndex:]


def merge_sort(l):
    if len(l) == 1 or len(l) == 0:
        return l
    else:
        mid = len(l)//2

        left = l[:mid]
        right = l[mid:]

        return merge(merge_sort(left), merge_sort(right))

l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
l = merge_sort(l)
print(l)