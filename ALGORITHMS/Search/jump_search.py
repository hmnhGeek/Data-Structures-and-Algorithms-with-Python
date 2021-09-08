def jump_search(arr, data, jump_size):
    '''This function assumes a sorted arr.'''

    if jump_size > len(arr) or jump_size <= 0:
        return "Invalid jump size"

    else:
        for i in range(0, len(arr), jump_size):
            if arr[i] > data:
                i = i - jump_size
                break
        
        for j in range(i, i+jump_size):
            if arr[j] == data:
                return j
        
        return -1

if __name__ == '__main__':
    l = [-3, 2, 8, 10, 17, 40, 100, 120]

    for i in l:
        print(jump_search(l, i, 4))

    print(jump_search(l, 16, 4))
    print(jump_search(l, 2, 7))
