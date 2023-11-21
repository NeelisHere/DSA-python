from typing import List
from tree import Node

class BST:
    def __init__(self, nodeList: List[int]):
        self.nodeList = nodeList
    
    def BSTutils(self, root: Node, nodeVal: int)->Node:
        if root is None:
            return Node(nodeVal)
        if nodeVal <= root.val:
            root.left = self.BSTutils(root.left, nodeVal)
        else:
            root.right = self.BSTutils(root.right, nodeVal)
        return root
    
    def buildBST(self)->Node:
        root = None
        for value in self.nodeList:
            root = self.BSTutils(root, value)
        return root  