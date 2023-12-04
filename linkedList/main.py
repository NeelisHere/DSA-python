from LinkedList import LinkedList, displayList
# from reverseLinkedList import reverseLinkedList
from findMiddle import findMiddle
# from detectCycle import detectCycle
from detectLoopStart import detectLoopStart

if __name__ == '__main__':
    l = LinkedList()
    for val in [12, 13, 14, 15, 16]:
        l.append(val)
    # displayList(l.head)
    fast, slow = findMiddle(l.head)
    fast.next = slow
    # print(fast.val, slow.val)
    ans = detectLoopStart(l.head)
    print(ans.val)