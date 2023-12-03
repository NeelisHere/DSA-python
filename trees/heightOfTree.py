def findHeight(root):
    if root is None: return -1
    return max(findHeight(root.left), findHeight(root.right)) + 1

def isBalanced(root):
    def utils(root):
        if root is None: return 0
        lh, rh = isBalanced(root.left), isBalanced(root.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1: return -1
        return max(lh, rh) + 1
    ans = utils(root)
    return True if ans != -1 else False