class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = new_node

  
def displayList(head):
    p = head
    res = []
    while p:
        res.append(p.val)
        p = p.next
    print(res)    

