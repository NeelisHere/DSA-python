from LinkedList import LinkedList, displayList, Node
# from reverseLinkedList import reverseLinkedList
# from findMiddle import findMiddle
# from detectCycle import detectCycle
# from detectLoopStart import detectLoopStart
# from removeDuplicate import removeDuplicate
# from checkPalindrome import checkPalindrome
from merge2SortedLists import merge2SortedLists
from mergeSort import mergeSort

if __name__ == '__main__':
    h1 = Node(7, Node(5, Node(6, Node(1, Node(2)))))
    # h2 = Node(7, Node(5, Node(6, Node(1, Node(2)))))
    h = mergeSort(h1)
    print(__name__)
    displayList(h)
    # displayList(merge2SortedLists(Node(6, Node(7)), Node(8)))
    # merge2SortedLists(h.head, p.head)
    