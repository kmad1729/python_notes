#!/usr/bin/env python3

'print all the paths from node to leaves in a binary tree'

from collections import deque

class BNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def print_in_order(self):
        if self != None:
            if self.left_child:
                self.left_child.print_in_order()
            print(self.data, end = " ")
            if self.right_child:
                self.right_child.print_in_order()

    def print_pre_order(self):
        if self != None:
            print(self.data, end = " ")
            if self.left_child:
                self.left_child.print_pre_order()
            if self.right_child:
                self.right_child.print_pre_order()

    def print_node_to_leaf(self, curr_list):
        if self != None:
            curr_list.append(self.data)
            if self.left_child:
                self.left_child.print_node_to_leaf(curr_list)
            if self.right_child:
                self.right_child.print_node_to_leaf(curr_list)
            if self.left_child == None and self.right_child == None:
                print(curr_list)
                curr_list.pop()
                return
            curr_list.pop()

    def depth(self):
        if self != None:
            if self.left_child != None:
                ldepth = self.left_child.depth()
            else:
                ldepth = 0
            if self.right_child != None:
                rdepth = self.right_child.depth()
            else:
                rdepth = 0
            return 1 + max(ldepth, rdepth)
        return 0

    def print_alternate_order(self):
        depth = self.depth()
        even_q = deque()
        odd_q = deque()
        if depth == 0:
            return
        even_q.append(self)
        for lvl in range(depth):
            if lvl % 2 == 0:
                while(len(even_q) != 0):
                    node = even_q.popleft()
                    if node.left_child != None:
                        odd_q.append(node.left_child)
                    if node.right_child != None:
                        odd_q.append(node.right_child)
                    print(node.data, end = " ")
            else:
                while(len(odd_q) != 0):
                    node = odd_q.pop()
                    if node.right_child != None:
                        even_q.appendleft(node.right_child)
                    if node.left_child != None:
                        even_q.appendleft(node.left_child)
                    print(node.data, end = " ")
        print()




class BTree:
    def __init__(self):
        self.root = None

    def print_in_order(self):
        self.root.print_in_order()
        print()

    def print_pre_order(self):
        self.root.print_pre_order()
        print()

    def print_node_to_leaf(self):
        if self.root == None:
            print()
        else:
            self.root.print_node_to_leaf([])

    def depth(self):
        if self.root != None:
            return self.root.depth()

    def print_alternate_order(self):
        if self.root != None:
            self.root.print_alternate_order()


class BSTree(BTree):

    def _insert_at_node(node, data):
        if node == None:
            return BNode(data)
        if data <= node.data:
            node.left_child = BSTree._insert_at_node(node.left_child, data)
        else:
            node.right_child = BSTree._insert_at_node(node.right_child, data)
        return node



    def insert(self, data):
        if self.root == None:
            self.root = BNode(data)
        else:
            self.root = BSTree._insert_at_node(self.root, data)



b1 = BSTree()
b1.insert(42)
b1.insert(98)
b1.insert(64)
b1.insert(86)
b1.insert(64)
b1.insert(16)
b1.insert(34)
b1.insert(2)
b1.insert(12)
b1.insert(-46)
b1.insert(50)

b1.print_in_order()
b1.print_pre_order()
b1.print_node_to_leaf()

print("depth of tree = ", b1.depth())

print('*' * 20)
print("alternate tree print -->")
b1.print_alternate_order()
print('*' * 20)

