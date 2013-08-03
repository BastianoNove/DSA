from counting import counting_sort
import random
import sys

def radix_sort(items):
    max_len = len(str(max(items)))
    def key_func(index):
        def _key(x):
            return (x/10**index) % 10
        return _key
    for i in range(max_len):
        items = counting_sort(items, 10, key_func(i))
    return items

def test():
    for x in range(1000):
        a = [random.randint(0,100) for i in range(10)]
        b = sorted(a)
        a = radix_sort(a)
        assert(all(a[i]==b[i] for i in range(len(a))))
    print('tests pass')

if __name__ == '__main__':
    test()

