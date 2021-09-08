def binary_search(arr, data, left, right):
    if arr == []:
        return -1
    else:
        if right >= left: # if this conditon is not provided, then stack will overflow
            mid = left + int((right - left)/2)

            if arr[mid] == data:
                return mid
            else:
                if data > arr[mid]:
                    return binary_search(arr, data, mid + 1, right)

                else:
                    return binary_search(arr, data, left, mid - 1)

        else:
            return -1

if __name__ == '__main__':
    l = [-3, 2, 8, 10, 17, 40, 100, 120]

    for i in l:
        print(binary_search(l, i, 0, len(l)-1))

    print(binary_search(l, 0, 0, len(l) - 1)) # returns -1