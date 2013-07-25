import random

class Heap(object):
    def __init__(self, a=None):
        self.A = []
        if a is not None:
            self.A.extend(a)
        self._size = len(self.A)-1
        self.build()

    def size(self):
        return self._size

    def heapify(self, i):
        assert(i>=0)
        left = i * 2 + 1
        right = i * 2 + 2
        if left <= self.size() and self.A[left] > self.A[i]:
            largest = left
        else:
            largest = i
        if right <= self.size() and self.A[right] > self.A[largest]:
            largest = right
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]
            self.heapify(largest)

    def build(self):
        for i in range(len(self.A)//2, 0, -1):
            self.heapify(i-1)

    def insert(self, x):
        self.A.append(x)
        self.heapify(self.size())

def check_heap(heap):
    for i in range(len(heap.A)//2):
        left = i * 2 + 1
        right = i * 2 + 2
        if left < heap.size():
            assert(heap.A[i] >= heap.A[left])
        if right < heap.size():
            assert(heap.A[i] >= heap.A[right])

def test():
    for i in range(1000):
        heap = Heap([random.randint(1,1000) for _ in range(random.randint(1, 100))])
        check_heap(heap)
    print('tests pass')

if __name__ == '__main__':
    test()
