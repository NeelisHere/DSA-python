def reverseLinkedList(head):
    if head.next is None or head is None:
        return head
    p = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return p
    