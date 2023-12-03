from collections import deque

class TreeView:
    def __init__(self):
        self.t = {}
        self.res = []

    # top-most node in a column
    def topView(self, root):
        if not root: return []
        q = deque([(root, 0)])
        while q:
            n = len(q)
            for _ in range(n):
                node, x = q.popleft()
                self.t[x] = self.t.get(x, []) + [node.val]
                if node.left: q.append((node.left, x-1))
                if node.right: q.append((node.right, x+1))
                
        for x in sorted(self.t):
            self.res.append(self.t[x][0])
            
        print(self.res)
    
    # bottom-most node in a column
    def bottomView(self, root):
        if not root: return []
        q = deque([(root, 0)])
        while q:
            n = len(q)
            for _ in range(n):
                node, x = q.popleft()
                self.t[x] = self.t.get(x, []) + [node.val]
                if node.left: q.append((node.left, x-1))
                if node.right: q.append((node.right, x+1))
                
        for x in sorted(self.t):
            self.res.append(self.t[x][-1])
            
        return self.res
    
    # left/right node in each horizontal level 
    def sideView(self, root, side=True):
        if not root: return []
        side = -1 if side else 0
        q = deque([root])
        while q:
            n = len(q)
            level = []
            for _ in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            self.res.append(level)
        self.res = list(map(lambda level: level[side], self.res))
        print(self.res)