class Node():
    def __init__(self, key):
        self.key = key 
        self.edges = []
        self.d = float('inf') #shortest path estimate
        self.predecessor = None
    def __repr__(self):
        return 'Node {0}, d {1}, predecessor {2}, edges {3}'.format(str(self.key),
          str(self.d), str(self.predecessor), str([x.key for x in self.edges]))
