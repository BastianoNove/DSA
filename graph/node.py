class Node():
    def __init__(self, key):
        self.key = key 
        self.edges = []
        self.d = float('inf') #shortest path estimate
        self.predecesor = None
