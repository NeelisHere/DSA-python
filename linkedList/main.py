from LinkedList import LinkedList, displayList
# from reverseLinkedList import reverseLinkedList
# from findMiddle import findMiddle
# from detectCycle import detectCycle
# from detectLoopStart import detectLoopStart
from removeDuplicate import removeDuplicate

if __name__ == '__main__':
    h1 = LinkedList()
    for node in [12,11,12,21,41,43,21]:
        h1.append(node)
    displayList(h1.head)
    removeDuplicate(h1.head)
    