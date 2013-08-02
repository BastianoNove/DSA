import random

def counting_sort(items, k, key=lambda x: x):
    L = [[] for i in range(k+1)]
    for j in range(len(items)):
        L[key(items[j])].append(items[j])
    output = []
    for i in range(k):
        output.extend(L[i])
    return output

def test():
    for _ in range(1000):
        a = [random.randint(0,100) for i in range(100)]
        b = sorted(a)
        a = counting_sort(a, max(a))
        assert(all(a[i] == b[i] for i in range(len(a))))
    print('tests pass')

if __name__ == '__main__':
    test()
