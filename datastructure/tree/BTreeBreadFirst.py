__author__ = 'FSG'
from collections import deque

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def breadthFirstSearch(root):
    queue = deque()
    queue.append(root)
    while len(queue) != 0:
        node = queue.popleft()
        print(node.value)
        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(0)
left = Node(1)
right = Node(2)
root.left = left
root.right = right
breadthFirstSearch(root)