'''You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.'''

def rob(l):
    amounts = [0]*len(l)

    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    elif len(l) == 2:
        return max(l)

    amounts[0], amounts[1] = l[0], max(l[0], l[1])

    for i in range(2, len(l)):
        amounts[i] = max(l[i] + amounts[i-2], amounts[i-1])

    return amounts[-1], amounts

l1 = [1,2,3,1]
l2 = [2,7,9,3,1]
l3 = [99,44,6,2,1,5,63,87,283,4,0]
l4 = [6, 7, 1, 3, 8, 2, 4]
l5 = [5, 3, 4, 11, 2]
l6 = [ 1, 3, 4, 4, 3, 3, 7, 2, 3, 4, 5, 1 ]

print(rob(l1))
print(rob(l2))
print(rob(l3))
print(rob(l4))
print(rob(l5))
print(rob(l6))