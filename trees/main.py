import traversals
from tree import Node

tree = Node(
    50, 
    Node(
        20, 
        Node(11), 
        Node(50)
    ), 
    Node(
        45, 
        Node(30), 
        Node(78)
    )
)

if __name__ == '__main__':
    traversals.inorder(tree)