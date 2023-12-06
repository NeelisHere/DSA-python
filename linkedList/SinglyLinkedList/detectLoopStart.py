from findMiddle import findMiddle
def detectLoopStart(head):
    fast = slow = head
    if not head: return head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow: break
    slow = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast