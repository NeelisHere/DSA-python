class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = Node(50, Node(20, Node(11), Node(50)), Node(45, Node(30), Node(78)))


output = []

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    output.append(root.val)
    inorder(root.right)
    
def preorder(root):
    if root is None:
        return
    output.append(root.val)
    inorder(root.left)
    inorder(root.right)

def postorder(root):
    if root is None:
        return
    inorder(root.left)
    inorder(root.right)
    output.append(root.val)
        



# inorder(tree) 
# print(output)

