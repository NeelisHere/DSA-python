def treeDiameter(root):
    print(__name__)
    res = 0
    def utils(root):
        nonlocal res
        if root is None: return 0
        lh, rh = utils(root.left), utils(root.right)
        res = max(res, lh + rh)
        return max(rh, lh) + 1
    
    utils(root)
    print(res)