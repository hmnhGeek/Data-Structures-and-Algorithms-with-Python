# first recurring character

def first_recurring_On(l):
    # O(n)
    first_time = []

    for i in l:
        if i not in first_time:
            first_time.append(i)

        else:
            return i
    
