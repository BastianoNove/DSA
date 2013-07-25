from heap import Heap
import random

def heap_sort(A):
    heap = Heap(A)
    while heap.size():
        heap.A[heap.size()], heap.A[0] = heap.A[0], heap.A[heap.size()]
        heap._size -= 1
        heap.heapify(0)
    return heap.A

def test():
    for i in range(1000):
        sequence = [random.randint(1,100) for _ in range(random.randint(1,100))]
        sorted_test = sorted(sequence)
        heap = heap_sort(sequence)
        assert(all(heap[i] == sorted_test[i] for i in range(len(sorted_test))))
    print('tests pass')

if __name__ == '__main__':
    test()
