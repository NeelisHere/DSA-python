from LinkedList import LinkedList, displayList

if __name__ == '__main__':
    l = LinkedList([12, 23, 34, 56, 67, 78])
    l.buildList()
    displayList(l.head)