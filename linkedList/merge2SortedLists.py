from LinkedList import Node, displayList
from detectCycle import detectCycle

# def merge2SortedLists(h1, h2):
#     if h1.val > h2.val: merge2SortedLists(h2, h1)
#     # print(__name__)
#     # displayList(h1)
#     # displayList(h2)
#     prev = Node(-1)
#     prev.next = h1
#     p1, p2 = h1, h2
#     while p2 and p1:
#         if p1.val <= p2.val:
#             p1 = p1.next
#             prev = prev.next
#         else:
#             prev.next = p2
#             prev = p2
#             p2 = p2.next
#             prev.next = p1
#     prev.next = p2
#     print(__name__, detectCycle(h1), detectCycle(h2))
#     displayList(h1)
#     # print(h1.val)
#     return h1


def merge2SortedLists(h1, h2):
	dummyNode = Node(0)
	tail = dummyNode
	while True:
		if h1 is None:
			tail.next = h2
			break
		if h2 is None:
			tail.next = h1
			break
		if h1.val <= h2.val:
			tail.next = h1
			h1 = h1.next
		else:
			tail.next = h2
			h2 = h2.next
		tail = tail.next
	return dummyNode.next