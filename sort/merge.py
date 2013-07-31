import random

def merge_sort(sequence):
    if len(sequence) == 1:
        return sequence
    l = merge_sort(sequence[:len(sequence)//2])
    r = merge_sort(sequence[len(sequence)//2:])
    merged = []
    while l and r:
        if l[0] < r[0]:
            merged.append(l[0])
            l = l[1:]
        else:
            merged.append(r[0])
            r = r[1:]
    merged.extend(l)
    merged.extend(r)
    return merged

def test():
    sequence = [int(1000*random.random()) for x in range(100)]
    test_sequence = sorted(sequence)
    sequence = merge_sort(sequence)
    assert(all(sequence[i] == test_sequence[i] for i in range(len(test_sequence))))
    print('tests pass')

if __name__ == '__main__':
    test()

