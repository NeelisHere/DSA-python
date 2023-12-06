from LinkedList import Node, displayList

def removeDuplicate(head):
    t = {}
    p = head
    prev = prev_backup = Node(-1)
    prev.next = prev_backup.next = p
    if not p: return 
    while p.next:
        # print(prev.val, p.val)
        if p.val in t:
            prev.next = p.next
            p = prev.next
        else:
            t[p.val] = True
            p = p.next
            prev = prev.next
    prev = prev_backup = None
    displayList(head)