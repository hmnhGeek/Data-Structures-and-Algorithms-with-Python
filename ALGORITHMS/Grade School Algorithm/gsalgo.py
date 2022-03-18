'''
Write a program which takes as input an array of digits encoding a nonnegative decimal integer
D and updates the array to represent the integer D + 1. For example, if the input is (1,2,9) then
you should update the array to (1,3,0). Your algorithm should work even if it is implemented in a
langua ge that has finite-precision arithmetic.
'''

def gs(l):
    if l[-1] == 9:
        l[-2] += 1
        l[-1] = 0
    else:
        l[-1] += 1
    
    return l

print(gs([1, 5, 9]))