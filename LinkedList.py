# Author: Zihan Li
# Date: 2020/2/18
# Description: a LinkedList class that has recursive implementations of the add, display, 
#              and remove methods described in the lesson.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_rec(self, node, val):
        if node is None:
            self.head = Node(val)
        else:
            if node.next is None:
                node.next = Node(val)
            else:
                self.add_rec(node.next, val)

    def add(self, val):
        self.add_rec(self.head, val)

    def display_rec(self, node):
        if node is None:
        # if current node is None, print a empty line
            print()
        else:
            print(node.data, end=" ")
            # print current node's data
            self.display_rec(node.next)
            # display from next node

    def display(self):
        self.display_rec(self.head)

    def remove_rec(self, prev, node, val):
        if node is None:
        # if current node is None, do nothing
            return
        else:
            if node.data == val:
            # if val found
                if prev is not None:
                    prev.next = node.next
                    # remove it
                else:
                    self.head = node.next
                self.remove_rec(prev, node.next, val)
                # remove from next
            else:
                self.remove_rec(node, node.next, val)
                # remove from next

    def remove(self, val):
        self.remove_rec(None, self.head, val)

    def is_empty(self):
        return self.head is None

    def contains_rec(self, node, val):
        if node is None:
        # if current node is none, return False
            return False
        else:
            if node.data == val:
            # if val found, return True
                return True
            else:
                return self.contains_rec(node.next, val)
                # find val from next node

    def contains(self, val):
        return self.contains_rec(self.head, val)

    def insert(self, idx, val):
        pass

    def reverse_rec(self, node):
        if node is None:
        # if node is None, do nothing
            return None

        next = node.next
        node.next = None

        if next is None:
        # if next node is None, return current node
            return node

        subhead = self.reverse_rec(next)
        # reverse from next node
        subtail = next
        subtail.next = node
        # add current node to the end of the reversed linked list
        return subhead

    def reverse(self):
        self.head = self.reverse_rec(self.head)
