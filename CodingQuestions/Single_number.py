# https://leetcode.com/problems/single-number/

def f(x):
    h = {}
    
    for i in x:
        if i not in h:
            h.update({i: 1})
        else:
            h.update({i: 2})
    
    for i, j in h.items():
        if j == 1:
            return i

l1 = [2,2,1]
l2 = [4,1,2,1,2]
l3 = [1]

print(f(l1))
print(f(l2))
print(f(l3))