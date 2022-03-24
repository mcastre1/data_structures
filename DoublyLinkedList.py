from DoublyLinkedListNode import DoublyLinkedListNode

a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

# We can also have a loop with doubly linked lists, by attaching the first to the last.