class SelectionSort:
    '''
        It is O(n^2) because of nested loops.
    '''
    
    def __init__(self, data):
        self.list = data

    def start(self):
        for i in range(len(self.list)):
            min_index = i

            for j in range(i+1, len(self.list)):
                if self.list[min_index] > self.list[j]:
                    min_index = j

            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]

def mergeTwoSortedArrays(l1, l2):
    l = l1+l2
    _selection_sort = SelectionSort(l)
    _selection_sort.start()
    return _selection_sort.list
