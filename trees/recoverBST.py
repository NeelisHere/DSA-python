from tree import Node
from queue import Queue
from typing import List
import traversals

def recoverBST(root: Node) -> None:
    if not root: return;
    arr = []
    def inorder(root: Node):
        if root: 
            inorder(root.left)
            arr.append(root)
            inorder(root.right)
    inorder(root)
    def compareNodes(node: Node):
        return node.val
    
    sorted_arr = sorted(arr, key=compareNodes)
    swappedNodes = []
    for i in range(len(arr)):
        if sorted_arr[i].val != arr[i].val:
            swappedNodes.append(arr[i])
    swappedNodes[0].val, swappedNodes[1].val = swappedNodes[1].val, swappedNodes[0].val 
