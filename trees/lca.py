def lca(root, p, q):
    if not root: 
        return None
    if root.val == p.val or root.val == q.val: 
        return root
    left, right = lca(root.left, p, q), lca(root.right, p, q)
    if left and right: 
        return root
    return left if left else right