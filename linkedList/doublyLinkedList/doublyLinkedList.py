class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

def appendNode(head, data):
    if head is None: return Node(data)
    next_node = appendNode(head.next, data)
    next_node.prev = head
    head.next = next_node
    return head

def buildList(arr):
    head = None
    for data in arr:
        head = appendNode(head, data)
    return head

def display(head):
    res = []
    p = head
    while p:
        res.append(str(p.data))
        p = p.next
    print('STAIGHT: ', ' '.join(res))
    tail = head
    while tail.next: tail = tail.next
    p = tail
    res = []
    while p:
        res.append(str(p.data))
        p = p.prev
    print('REVERSE: ', ' '.join(res))    
    
