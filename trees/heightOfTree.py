def findHeight(root):
    if root is None: return -1
    return max(findHeight(root.left), findHeight(root.right)) + 1
