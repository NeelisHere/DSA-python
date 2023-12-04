from LinkedList import Node, displayList
from detectCycle import detectCycle

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