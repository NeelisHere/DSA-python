from LinkedList import Node, displayList

def mergeSortedLists(h1, h2):
    if h1.val > h2.val: mergeSortedLists(h2, h1)
    prev = Node(-1)
    prev.next = h1
    p1, p2 = h1, h2
    while p2 and p1:
        if p1.val <= p2.val:
            p1 = p1.next
            prev = prev.next
        else:
            prev.next = p2
            prev = p2
            p2 = p2.next
            prev.next = p1
    prev.next = p2
    displayList(h1)