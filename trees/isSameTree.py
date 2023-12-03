def isSameTree(root1, root2):
    def utils(root1, root2):
        if not root1 and not root2: return True
        if not root1 or not root2: return False
        l, r = utils(root1.left, root2.left), utils(root1.right, root2.right)
        return l and r
    print(utils(root1, root2))