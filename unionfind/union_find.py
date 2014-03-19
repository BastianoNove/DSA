class Node(object):
    def __init__(self, data, parent=None, rank=0):
        self.data = data
        self.rank = rank
        self.parent = parent

class UnionFind(object):
    def __init__(self, words):
        self.network = dict()
        for word in words:
            self.network[word] = Node(word)

    def find(self, node):
        '''Returns root of the tree this node belongs to '''
        while node.parent:
            node = node.parent
        return node

    def union(self, a, b):
        '''Merge a's tree with b's tree
           Returns root of merged tree
        '''
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return root_a

        root_a.parent = root_b
        return root_b

def test():
    words = 'the are test edit long distance flight word western pieces'.split()
    uf = UnionFind(words)
    are = uf.network['are']
    flight = uf.network['flight']
    pieces  = uf.network['pieces']
    distance = uf.network['distance']

    assert(are.parent == None)
    assert(distance.parent == None)
    uf.union(are, distance)
    assert(uf.find(are) == uf.find(distance))
    uf.union(pieces, distance)
    uf.union(pieces, flight)
    uf.union(are, flight)
    assert(uf.find(distance) == uf.find(flight))
    print 'tests pass'

if __name__ == '__main__':
    test()

