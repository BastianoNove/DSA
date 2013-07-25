from heap import Heap
import random

def heap_sort(A):
    heap = Heap(A)
    while heap.size():
        heap.A[heap.size()], heap.A[1] = heap.A[1], heap.A[heap.size()]
        heap._size -= 1
        heap.heapify(0)
    return heap.A

def test():
    sequence = [random.randint(1,100) for _ in range(5)]
    print(sequence)
    sequence = heap_sort(sequence)
    print(sequence)
test()
