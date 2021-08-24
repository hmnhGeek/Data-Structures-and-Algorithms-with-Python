def getSumIndices_On2(data, addSum):
    complement = []

    for i in range(len(data)):
        for j in range(len(data)):
            if data[i]+data[j] == addSum and i != j:
                return i, j

def getSumIndices_On(data, addSum):
    D = {i: data.index(i) for i in data}

    for i in range(len(data)):
        if addSum - data[i] in D:
            if i != D[addSum - data[i]]:
                return i, D[addSum - data[i]]
    return None
            
