class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def CC(N):
    head = temp = Node(1)
    for i in range(1,N+1):
        curr = Node(i)
        if(head== None):
            head = curr
            temp = head
        else:
            temp.next = curr
        temp = temp.next
    return head.next

head = CC(5)
while(head!=None):
    print(head.data)
    head = head.next
