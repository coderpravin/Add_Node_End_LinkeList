class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleBegNode(head):
    if head is None:
        return None
    
    return head.next
    
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
head = deleBegNode(head)

printList(head)


