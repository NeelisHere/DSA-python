
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
        



