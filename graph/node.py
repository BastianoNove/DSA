class Node():
    def __init__(self, key):
        self.key = key 
        self.edges = []
        self.d = float('inf') #shortest path estimate
        self.predecessor = None
    def __repr__(self):
        predecessor = self.predecessor.key if self.predecessor else None
        return 'Node {0}, d {1}, predecessor {2}, edges {3}'.format(str(self.key),
          str(self.d), str(predecessor), str([x.key for x in self.edges]))
