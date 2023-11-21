from tree import Node
# import traversals
# import uniqueBinaryTrees as ubt
from targetSum import targetSum

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

if __name__ == '__main__':
    # traversals.inorder(tree)
    print(targetSum(tree2, 22))