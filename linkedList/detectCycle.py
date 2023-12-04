def detectCycle(head):
    fast = slow = head
    if not head: return False
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: return True
    return False
    
    
    