def findMiddle(head):
    fast = slow = head
    if not head: return (fast, slow)
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next: fast = fast.next
    return (fast, slow)