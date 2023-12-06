from reverseLinkedList import reverseLinkedList
from LinkedList import displayList

def checkPalindrome(head):
    fast = slow = head
    if not fast or not fast.next: print(False)
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    while fast.next: fast = fast.next
    slow.next = reverseLinkedList(slow.next)
    slow = slow.next
    p = head
    displayList(p)
    while slow:
        if p.val != slow.val: 
            print(False)
            break
        p = p.next
        slow = slow.next
    print(True)       
            
            
            