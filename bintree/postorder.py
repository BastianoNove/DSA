from bintree import BinaryTree

def postorder(node, visit=print):
    if node is None:
        return
    postorder(node.left, visit)
    postorder(node.right, visit)
    visit(node.key)

def postorder_iterative(node, visit=print):
    stack = [node]
    visited = []
    while stack:
        curr_item = stack[-1]
        if curr_item.right:
            if curr_item.right not in visited:
              stack.append(curr_item.right)
        if curr_item.left:
            if curr_item.left not in visited:
                stack.append(curr_item.left,)
        if (((curr_item.left in visited) or curr_item.left is None) and 
                (curr_item.right in visited or curr_item.right is None)):
            visit(curr_item.key)
            visited.append(curr_item)
            stack.pop()

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
    postorder(root)
    print()
    postorder_iterative(root)

        
