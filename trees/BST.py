from tree import Node

def insertNode(root, val):
    if root is None: return Node(val)
    else:
        if val <= root.val: root.left = insertNode(root.left, val)
        else: root.right = insertNode(root.right, val)
        return root
    
def bst(arr):
    root = None
    for val in arr:
        root = insertNode(root, val) 
    return root