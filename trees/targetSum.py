
def targetSum(root, target):
    output = []
    def solve(root, arr, target):
        if root is None: return
        arr.append(root.val)
        x = target - root.val
        # if x < 0: return
        if x == 0: output.append(arr.copy())
        solve(root.left, arr, x)
        solve(root.right, arr, x)
        arr.pop()
    
    solve(root, [], target)
    return output