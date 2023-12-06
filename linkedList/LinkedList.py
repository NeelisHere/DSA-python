class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
        
def append(head, value):
    if head is None:
        return Node(value)
    head.next = append(head.next, value)
    return head 

def buildList(arr):
    h = None
    for val in arr:
        h = append(h, val)
    return h
  
def displayList(head):
    p = head
    res = []
    while p:
        res.append(p.val)
        p = p.next
    print(' '.join(list(map(lambda x: str(x), res))))    

