__author__ = 'FSG'
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def depthFisrt(root):
    stack = []
    stack.append(root)
    while len(stack) != 0:
        node = stack.pop()
        print(node.value)

        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

root = Node(0)
left = Node(1)
right = Node(2)
rright = Node(3)
right.right = rright
root.left = left
root.right = right

depthFisrt(root)