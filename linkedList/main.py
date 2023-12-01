from LinkedList import LinkedList, displayList
from reverseLinkedList import reverseLinkedList

if __name__ == '__main__':
    l = LinkedList()
    for val in [12, 13, 14, 15, 16, 17]:
        l.append(val)
    # l.buildList()
    displayList(l.head)
    l.head = reverseLinkedList(l.head)
    displayList(l.head)
    