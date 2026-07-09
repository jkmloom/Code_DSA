# Singly Linked List
# A collection of nodes ordered by links (pointers) rather than physical memory placement.
# Pro-> list can be extended until memory is full
# Corn-> we can't go back in memory

class Node:
    # we are creating our own data type
    # user defined data type
    def __init__(self, info, next=None):
        self.data = info
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert_at_end(self, value):
        Node(30)