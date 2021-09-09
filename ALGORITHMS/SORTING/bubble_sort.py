def bubble_sort(l):
    for i in range(len(l)):
        there_was_a_pass = False # this variable is for breaking the loop if no pass happened.
        swaps = 0

        for j in range(len(l)-1): # go upto len -1 because the last element will be compared.
            if l[j+1] < l[j]:
                l[j], l[j+1] = l[j+1], l[j]
                there_was_a_pass = True
                swaps += 1
        
        print(f"Total swaps in {i+1} pass = {swaps}.")
        
        if not there_was_a_pass:
            return l
    
    return l

l = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
l = bubble_sort(l)

print(l)