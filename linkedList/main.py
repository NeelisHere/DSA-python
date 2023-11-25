from LinkedList import LinkedList, displayList
from reverseLinkedList import reverseLinkedList

if __name__ == '__main__':
    l = LinkedList([1, 2, 3, 4, 5, 6])
    l.buildList()
    displayList(l.head)
    l.head = reverseLinkedList(l.head)
    displayList(l.head)
    