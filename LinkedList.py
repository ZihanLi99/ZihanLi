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
        # if current node is None, print a empty line
        if node is None:
            print()
        else:
            # print current node's data
            print(node.data, end=" ")
            # display from next node
            self.display_rec(node.next)

    def display(self):
        self.display_rec(self.head)

    def remove_rec(self, prev, node, val):
        # if current node is None, do nothing
        if node is None:
            return
        else:
            # if val found
            if node.data == val:
                # remove it
                if prev is not None:
                    prev.next = node.next
                else:
                    self.head = node.next
                # remove from next
                self.remove_rec(prev, node.next, val)
            else:
                # remove from next
                self.remove_rec(node, node.next, val)

    def remove(self, val):
        self.remove_rec(None, self.head, val)

    def is_empty(self):
        return self.head is None

    def contains_rec(self, node, val):
        # if current node is none, return False
        if node is None:
            return False
        else:
            # if val found, return True
            if node.data == val:
                return True
            else:
                # find val from next node
                return self.contains_rec(node.next, val)

    def contains(self, val):
        return self.contains_rec(self.head, val)

    def insert(self, idx, val):
        pass

    def reverse_rec(self, node):
        # if node is None, do nothing
        if node is None:
            return None

        next = node.next
        node.next = None

        # if next node is None, return current node
        if next is None:
            return node

        # reverse from next node
        subhead = self.reverse_rec(next)
        subtail = next
        # add current node to the end of the reversed linked list
        subtail.next = node
        return subhead

    def reverse(self):
        self.head = self.reverse_rec(self.head)
