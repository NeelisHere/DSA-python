def reversePairs(head):
    if head is None or head.next is None:
        return head
    temp = head.next
    head.next = reversePairs(head.next.next)
    temp.next = head
    return temp