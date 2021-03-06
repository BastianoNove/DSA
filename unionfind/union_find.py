class Node(object):
    def __init__(self, data, parent=None, rank=0, count=1):
        self.data = data
        self.rank = rank
        self.count = count
        self.parent = parent

class UnionFind(object):
    def __init__(self, words):
        self.network = dict()
        for word in words:
            self.network[word] = Node(word)

    def find(self, node):
        '''Returns root of the tree this node belongs to '''
        if node.parent is not None:
            node.parent = self.find(node.parent)
        elif node.parent is None:
            return node
        return node.parent

    def union(self, a, b):
        '''Merge a's tree with b's tree
           Returns root of merged tree
        '''
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return root_a
        if root_a.rank > root_b.rank:
            root_b.parent = root_a
            root_a.count = root_b.count + root_a.count
            return root_a

        if root_a.rank == root_b.rank:
            root_b.rank += 1
        root_a.parent = root_b
        root_b.count = root_a.count + root_b.count
        return root_b

def test():
    words = 'the are test edit long distance flight word western pieces'.split()
    uf = UnionFind(words)
    are = uf.network['are']
    flight = uf.network['flight']
    pieces  = uf.network['pieces']
    distance = uf.network['distance']
    test = uf.network['test']
    the = uf.network['the']

    assert(are.parent == None)
    assert(distance.parent == None)
    uf.union(are, distance)
    assert(uf.find(are) == uf.find(distance))
    uf.union(pieces, distance)
    uf.union(pieces, flight)
    uf.union(are, flight)
    assert(uf.find(distance) == uf.find(flight))
    distance_root = uf.find(distance)
    assert(distance_root and distance_root.rank == 1)
    uf.union(test, the)
    uf.union(the, distance)
    assert(uf.find(test) == distance)
    print 'tests pass'

if __name__ == '__main__':
    test()

