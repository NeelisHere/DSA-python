from queue import Queue

def countGoodNodes(root):
    def solve(root):
        res, q = 0, Queue()
        q.put((root, root.val)) # (value, max_value_so_far)
        while not q.empty():
            node, maxVal = q.get()
            if node.val >= maxVal: 
                res += 1
                print(node.val)
            if node.left: q.put((node.left, max(node.left.val, maxVal)))
            if node.right: q.put((node.right, max(node.right.val, maxVal)))
            
        return res
    
    return solve(root)