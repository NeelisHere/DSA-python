from LinkedList import displayList
from merge2SortedLists import merge2SortedLists

def mergeSort(head):
    if not head.next: return head
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    mid = slow
    slow = slow.next
    h1, h2 = head, slow
    mid.next = mid = None
    left, right = mergeSort(h1), mergeSort(h2)
    return merge2SortedLists(left, right)