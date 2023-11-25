class Node:
    def __init__(self, value, next=None):
        self.val = value
        self.next = next
        
class LinkedList:
    def __init__(self, list):
        self.list = list
        self.head = None
    
    def buildListUtils(self, index):
        if index == len(self.list):return
        return Node(self.list[index], self.buildListUtils(index + 1))
        
    def buildList(self):
        if len(self.list):
            self.head = self.buildListUtils(0)

  
def displayList(head):
    p = head
    displayString = ''
    while p:
        displayString += f'{p.val}->'
        p = p.next
    print(displayString[:-2])    

