def get_largest_sum_sub_array_o_n_2(l):
    maxSum = sum(l)
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            sub_list = l[i:j]
            if sum(sub_list) > maxSum:
                maxSum = sum(sub_list)
    
    return maxSum

def get_largest_sum_sub_array_o_n(l):
    currSum, maxSum = 0, -10000

    for i in l:
        currSum += i
    
        if currSum > maxSum:
            maxSum = currSum

        if currSum < 0:
            currSum = 0

    return maxSum

print(get_largest_sum_sub_array_o_n([-2,1,-3,4,-1,2,1,-5,4]))
print(get_largest_sum_sub_array_o_n([5,4,-1,7,8]))