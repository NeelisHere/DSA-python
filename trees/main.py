from tree import Node
import traversals
# from heightOfTree import *
# from recoverBST import recoverBST
# import uniqueBinaryTrees as ubt
# from targetSum import targetSum
# from countGoodNodes import countGoodNodes
# from BST import bst
# from treeDiameter import treeDiameter
from isSameTree import isSameTree

tree1 = Node(
    5, 
    Node(
        2, 
        Node(1), 
        Node(8)
    ), 
    Node(
        4, 
        Node(3), 
        Node(7)
    )
)

tree2 = Node(
    5, 
    Node(
        4, 
        Node(
            11,
            Node(7),
            Node(2)
        ),
        Node(3),
    ), 
    Node(
        8,
        Node(13), 
        Node(
            4,
            Node(5),
            Node(1)
        )
    )
)

tree = Node(1, Node(3, None, Node(2)))

if __name__ == '__main__':
    # root = bst([5,6,7,8,1,2,3,4])
    # traversals.inorder(tree2)
    isSameTree(tree2, tree1)
    