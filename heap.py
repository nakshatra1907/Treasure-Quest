class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function, init_array):
        self.comp = comparison_function
        self.heap = init_array
        n = len(init_array)
        for i in range(n // 2 - 1, -1, -1):
            self.downheap(i)

    def downheap(self, index):
        n = len(self.heap)
        walk = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < n and self.comp(self.heap[left_child_index], self.heap[walk]):
            walk = left_child_index
        if right_child_index < n and self.comp(self.heap[right_child_index], self.heap[walk]):
            walk = right_child_index
        if walk != index:
            self.heap[walk], self.heap[index] = self.heap[index], self.heap[walk]
            self.downheap(walk)

    def upheap(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.comp(self.heap[index], self.heap[parent_index]):
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2
            
    def insert(self, value):
        self.heap.append(value)
        self.upheap(len(self.heap) - 1)

    def extract(self):
        if self.size() == 0:
            return None
        root = self.top()
        last = self.heap.pop()
        if self.size() > 0:
            self.heap[0] = last
            self.downheap(0)
        return root
            
    def top(self):
        if self.size() == 0:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)
