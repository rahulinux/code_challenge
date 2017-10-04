#!/usr/bin/env python

class Node:
    # Function to initilize the node object
    def __init__(self,data):
        self.data = data # Assign data
        self.next = None # initilized next as null 



class LinkedList:

    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print temp.data
            temp = temp.next
            
    def reverse(self):
        new_head = None
        while self.head:
            self.head.next, self.head, new_head = new_head, self.head.next, self.head
        self.head = new_head


if __name__ == '__main__':

    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Link first node with second
    llist.head.next = second
    # Link second node with third
    second.next = third 
    llist.reverse()
    llist.printList()
