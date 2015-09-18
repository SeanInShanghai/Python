__author__ = 'FSG'
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    """Pre traverse the binary tree with
    :param root:the root of the binary tree
    :type Node

    :return None
    """
    if None == root:
        return

    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def preTraverse2(root):
    """Pre Traverse with non-recursion function

    :param root:
    :return None
    """
    tmp = root
    stack = []
    while tmp or len(stack) != 0:
        if tmp != None:
            print(tmp.value)
            stack.append(tmp.right)
            tmp = tmp.left
        else:
            tmp = stack[-1]
            stack.pop()


def inTraverse(root):
    """In order traverse tree

    :param root:
    :return:
    """
    if root == None:
        return

    inTraverse(root.left)
    print(root.value)
    inTraverse(root.right)

def inTraverse2(root):
    """In order traverse binary tree non-recursion function

    :param root:
    :return:
    """
    stack = []
    tmp = root
    while tmp or len(stack) != 0:
        if tmp!= None:
            stack.append(tmp)
            tmp = tmp.left
        else:
            tmp = stack.pop()
            print(tmp.value)
            tmp = tmp.right

def postTraverse(root):
    """Post order traverse

    :param root:
    :return:
    """
    if root == None:
        return
    postTraverse(root.left)
    postTraverse(root.right)
    print(root.value)

def postTraverse2(root):
    """Post order traverse non-recursion function

    :param root:
    :return:
    """
    stack = []
    tmp = root

    while tmp or len(stack) != 0:
        if tmp != None:
            stack.append(tmp)
            stack.append(tmp.right)
            tmp = tmp.left
        else:
            tmp = stack.pop()
            if tmp != None:
                tmp = stack.pop()
                print(tmp.value)
                if len(stack) == 0:
                    break
                tmp = stack.pop()
            stack.append(None)


root = Node()
root.value = 0
node1 = Node()
node1.value = 1
root.left=node1
node2 = Node()
node2.value = 2
root.right = node2

preTraverse(root)
preTraverse2(root)
inTraverse(root)
inTraverse2(root)

postTraverse(root)
postTraverse2(root)