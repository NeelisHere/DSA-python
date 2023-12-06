from LinkedList import buildList, displayList
# from reverseLinkedList import reverseLinkedList
# from findMiddle import findMiddle
# from detectCycle import detectCycle
# from detectLoopStart import detectLoopStart
# from removeDuplicate import removeDuplicate
# from checkPalindrome import checkPalindrome
# from merge2SortedLists import merge2SortedLists
# from mergeSort import mergeSort
from reversePairs import reversePairs

if __name__ == '__main__':
    h1 = buildList([1,2,3,4,5])
    h2 = buildList([1,2,3,4])
    displayList(h1)
    displayList(h2)
    h1 = reversePairs(h1)
    h2 = reversePairs(h2)
    displayList(h1)
    displayList(h2)