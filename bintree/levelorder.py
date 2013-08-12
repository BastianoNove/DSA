from bintree import BinaryTree
from collections import deque

def levelorder(node, visit=print, queue = None):
    if queue is None:
        queue = deque([node])
    curr_item = queue.popleft()
    visit(curr_item.key)
    if curr_item.left:
        queue.append(curr_item.left)
    if curr_item.right:
        queue.append(curr_item.right)
    if queue:
        levelorder(None, visit, queue)

def levelorder_iterative(node, visit=print):
    queue = deque()
    queue.append(node)
    while queue:
        curr_item = queue.popleft()
        visit(curr_item.key)
        if curr_item.left:
            queue.append(curr_item.left)
        if curr_item.right:
            queue.append(curr_item.right)

if __name__ == '__main__':
    root = BinaryTree('F')
    root.left = BinaryTree('B')
    root.right = BinaryTree('G')
    root.left.left = BinaryTree('A')
    root.left.right = BinaryTree('D')
    root.left.right.left = BinaryTree('C')
    root.left.right.right = BinaryTree('E')
    root.right.right = BinaryTree('I')
    root.right.right.left = BinaryTree('H')
    levelorder(root)
    print()
    levelorder_iterative(root)

