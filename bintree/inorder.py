from bintree import BinaryTree

def inorder(node, visit=print):
    if node is None:
        return
    inorder(node.left, visit)
    visit(node.key)
    inorder(node.right, visit)

def inorder_iterative(node, visit=print):
    stack = [node]
    visited = []
    while stack:
        curr_item = stack[-1]
        if curr_item.left is None or curr_item.left in visited:
            visit(curr_item.key)
            visited.append(curr_item)
            stack.pop()
            if curr_item.right:
                stack.append(curr_item.right)
        else:
            if curr_item not in visited:
                stack.append(curr_item.left)

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
    inorder(root)
    print()
    inorder_iterative(root)

