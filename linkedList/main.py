from LinkedList import LinkedList, displayList
# from reverseLinkedList import reverseLinkedList
# from findMiddle import findMiddle
# from detectCycle import detectCycle
# from detectLoopStart import detectLoopStart
# from removeDuplicate import removeDuplicate
# from checkPalindrome import checkPalindrome
from mergeSortedLists import mergeSortedLists

if __name__ == '__main__':
    h1 = LinkedList()
    h2 = LinkedList()
    for node in [1,2,3,4,5]:
        h1.append(node)
        h2.append(node)
    displayList(h1.head)
    displayList(h2.head)
    mergeSortedLists(h1.head, h2.head)
    