def lca_bst(root, p, q):
    if not root: return root
    if root.val < p.val and root.val < q.val:
        return lca_bst(root.right, p, q)
    elif root.val > p.val and root.val > q.val:
        return lca_bst(root.left, p, q)
    else:
        return root