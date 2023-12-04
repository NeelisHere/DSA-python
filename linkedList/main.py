from LinkedList import LinkedList, displayList
# from reverseLinkedList import reverseLinkedList
# from findMiddle import findMiddle
# from detectCycle import detectCycle
# from detectLoopStart import detectLoopStart
# from removeDuplicate import removeDuplicate
from checkPalindrome import checkPalindrome

if __name__ == '__main__':
    h1 = LinkedList()
    for node in [1,2,2,1]:
        h1.append(node)
    displayList(h1.head)
    checkPalindrome(h1.head)
    