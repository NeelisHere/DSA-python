from collections import deque

def inorder(root):
    output = []
    def solve(root):
        if root is None:
            return
        solve(root.left)
        output.append(root.val)
        solve(root.right)
    solve(root)
    print(output)
    
def preorder(root):
    output = []
    def solve(root):
        if root is None:
            return
        output.append(root.val)
        solve(root.left)
        solve(root.right)
    solve(root)
    print(output)

def postorder(root):
    output = []
    def solve(root):
        if root is None:
            return
        solve(root.left)
        solve(root.right)
        output.append(root.val)
    solve(root)
    print(output)
        
def zigzagLevelOrder(root):
    if not root: return []
    res = []
    q = deque([root])
    toggle = False
    while q:
        level = []
        n = len(q)
        for _ in range(n):
            node = q.popleft()
            level.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        if toggle: level.reverse()
        res.append(level)
        toggle = not toggle
    print(res)

def verticalTraversal(root):
    t = {}
    res = []
    q = deque([(root, 0, 0)])
    
    while q:
        node, x, y = q.popleft()
        if x in t: t[x].append((y, node.val))
        else: t[x] = [(y, node.val)]
        if node.left: q.append((node.left, x - 1, y + 1))
        if node.right: q.append((node.right, x + 1, y + 1))

    for _, value in sorted(list(t.items())):
        value.sort()
        temp = []
        for _, x in value: temp.append(x)
        res.append(temp)

    return res
