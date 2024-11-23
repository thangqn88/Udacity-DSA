class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(2)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)

def print_linked_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next

print_linked_list(head)