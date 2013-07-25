import random

def insertion_sort(sequence):
    '''Implementation of insertion sort'''
    for key in range(2, len(sequence)+1):
        for i in range(key-1, 0, -1):
            if sequence[i-1] <= sequence[i]:
                break;
            sequence[i-1], sequence[i] = sequence[i], sequence[i-1]

def test():
    sequence = [1000*random.random() for x in range(100)]
    test_sequence = sorted(sequence)
    insertion_sort(sequence)
    assert(all(sequence[i] == test_sequence[i] for i in range(len(sequence))))
    print('tests pass')

test()
