#Binary Tree implemented by non-retrived funciton
class TreeNode(object):
    def __init__(self,left=0, right=0, data=0):
        self.left = left
        self.right = right
        self.data = data
    
class BTree(object):
    def __init__(self,root=0):
        self.root = root

    def is_empty(self):
        if self.root is 0:
            return True
        else:
            return False

    def preOrder(self, treenode):
        stack = []
        while treenode or stack:
            if treenode is not 0:
                print treenode.data
                stack.append(treenode)
                treenode = treenode.left
            else:
                treenode = stack.pop()
                treenode = treenode.right

    def inOrder(self, treenode):
        stack = []
        while treenode or stack:
            if treenode:
                stack.append(treenode)
                treenode = treenode.left
            else:
                treenode = stack.pop()
                print treenode.data
                treenode = treenode.right

    def postOrder(self,treenode):
        stack = []
        queue = []
        queue.append(treenode)
        while queue:
            treenode = queue.pop()
            if treenode.left:
                queue.append(treenode.left)
            if treenode.right:
                queue.append(treenode.right)
            stack.append(treenode)
        while stack:
            print stack.pop().data

    def levelOrder(self,treenode):
        from collections import deque
        if not treenode:
            return
        q = deque([treenode])
        while q:
            treenode = q.popleft()
            print treenode.data
            if treenode.left:
                q.append(treenode.left)
            if treenode.right:
                q.append(treenode.right)

node1 = TreeNode(data=1)
node2 = TreeNode(node1,0,2)
node3 = TreeNode(data=3)
node4 = TreeNode(data=4)
node5 = TreeNode(node3,node4,5)
node6 = TreeNode(node2,node5,6)
node7 = TreeNode(node6,0,7)
node8 = TreeNode(data=8)
root = TreeNode(node7,node8,'root')

bt = BTree(root)

print 'pre-Order...'
bt.preOrder(bt.root)
print 'in-Order...'
bt.inOrder(bt.root)
print 'post-order...'
bt.postOrder(bt.root)
print 'level-order...'
bt.levelOrder(bt.root)
