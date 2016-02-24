#!/usr/bin/env python3

'print all the paths from node to leaves in a binary tree'

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



class BSTree(BTree):

    def _insert_at_node(node, data):
        if node == None:
            return BNode(data)
        if data < node.data:
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



