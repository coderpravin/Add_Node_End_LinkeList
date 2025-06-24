class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def addNodeEnd(head, x):
    temp = Node(x)
    if head is None:
        return temp
    current = head
    while current is not None:
        current = current.next
    current.next = temp
    return head

def printList(head):
    if head is None:
        return None
    current = head
    while current is not None:
        print(current.data)
        current = current.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4
    

head = node1
head = addNodeEnd(head, x=50)
printList(head)