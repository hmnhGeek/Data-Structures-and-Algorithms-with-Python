# given two arrays, find if there is any common element in them

## KEY POINTS ##
'''
1. The arrays may or may not be sorted.
2. The function takes these two arrays as inputs and return True/False as output.
'''

## MAIN GOAL ##
# write the most efficient function, both in terms of space and time complexity.

## NAIVE APPROACH ##
# The naive approach is to use two for-loops. The parent loop will take up element
# from the first array and the nested loop will loop on the elements of the second
# array and then the comparison happens. This is O(m*n) approach.

def naive_approach(arr1, arr2):
    for item1 in arr1: # O(n)
        for item2 in arr2: # O(m)
            if item1 == item2:
                return True
    return False

    # net complexity O(n*m)

## BETTER APPROACH ##
# Create a hash (dictionary) to such that if arr1 = [1,2,3,4] then dictionary should be
# {1: True, 2: True, 3: True, 4: True}. This can be done using looping on the first array.
# Now loop on second array and check if dictionary[arr2[i]] == True.

def better_approach(arr1, arr2):
    map_dict = {i:True for i in arr1} # O(n)

    for j in arr2: # O(m)
        try:
            if map_dict[j]:
                return True
        except KeyError:
            continue
    return False

    # net complexity is O(n + m)

if __name__ == '__main__':
    l1 = ['a', 'b', 2, 0, None]
    l2 = ['x', None, 'z']

    # using naive approach
    print("Using naive approach... O(n*m) time complexity...")
    print(naive_approach(l1, l2))

    # using better approach
    print("Using naive approach... O(n + m) time complexity...")
    print(better_approach(l1, l2))