#!/usr/bin/env python3
from random import randint

class Node:
    def __init__(self, new_value):
        self.value = new_value
        self.left = None
        self.right = None

    def insert(self, new_value):
        if self.value == new_value:
            return False
        elif new_value < self.value:
            if self.left:
                return self.left.insert(new_value)
            else:
                self.left = Node(new_value)
                return True
        else: # new_value > self.value
            if self.right:
                return self.right.insert(new_value)
            else:
                self.right = Node(new_value)
                return True

    def find(self, sought_value):
        if self.value == sought_value:
            return True
        elif sought_value < self.value:
            return self.left and self.left.find(sought_value)
        else:
            return self.right and self.right.find(sought_value)

    def remove(self, remove_value, parent=None):
        if remove_value < self.value:
            return (self.left
                and self.left.remove(remove_value, self))
        elif remove_value > self.value:
            return (self.right
                and self.right.remove(remove_value, self))
        else:  # remove_value == self.value
            if not self.left and not self.right:
                self = None
            elif self.left and not self.right:
                if not parent: # removing root
                    self = self.left
                elif parent.left == self:
                    parent.left = self.left
                else:
                    parent.right = self.left
            elif self.right and not self.left:
                if not parent: # removing root
                    self = self.right
                elif parent.left == self:
                    parent.left = self.right
                else:
                    parent.right = self.right
            else: # left and right children present
                # find minimum in right branch
                min_right_parent = self
                min_right = self.right
                right = True
                while min_right.left:
                    right = False
                    min_right_parent = min_right
                    min_right = min_right.left
                # remove it and place its value in the place of removed value
                if min_right.right:
                    min_right_parent.right = min_right.right
                self.value = min_right.value
                if right:
                    min_right_parent.right = min_right.right
                else:
                    min_right_parent.left = None
            return True

    def __str__(self):  # quick and sloppy!!!
        node_string = 'node: {}'.format(str(self.value))
        if self.left:
            node_string += ', left: {}'.format(str(self.left.value))
        if self.right:
            node_string += ', right: {}'.format(str(self.right.value))
        node_string += '\n'
        # recurse
        if self.left:
            node_string += str(self.left)
        if self.right:
            node_string += str(self.right)
        return node_string


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        return self.root and self.root.find(value)

    def remove(self, value):
        return self.root and self.root.remove(value)

    def __str__(self):
        return str(self.root)

    def pre_order_traversal(self):
        # iterative: not similarity to dfs!
        values = []
        node_stack = []
        node_stack.append(self.root)
        while len(node_stack) > 0:
            node = node_stack.pop()
            values.append(node.value)
            for n in [node.right, node.left]:
                if n: node_stack.append(n)
        return values

        # recursive:
        # def _pre_order_helper(node, values):
        #     values.append(node.value)
        #     if node.left: _pre_order_helper(node.left, values)
        #     if node.right: _pre_order_helper(node.right, values)
        #     return values
        #
        # return _pre_order_helper(self.root, [])

    def in_order_traversal(self):
        # recursive:
        def _in_order_helper(node, values):
            if node.left: _in_order_helper(node.left, values)
            values.append(node.value)
            if node.right: _in_order_helper(node.right, values)
            return values

        return _in_order_helper(self.root, [])

    def post_order_traversal(self):
        def _post_order_helper(node, values):
            if node.left: _post_order_helper(node.left, values)
            if node.right: _post_order_helper(node.right, values)
            values.append(node.value)
            return values

        return _post_order_helper(self.root, [])


if __name__ == '__main__':

    tree = BST()
    print (str(tree) + '\n')

    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.insert(9)
    print (str(tree))
    print (tree.pre_order_traversal())
    print (tree.in_order_traversal())
    print (tree.post_order_traversal())

    # print ()
    #
    # tree.remove(3)
    # print (str(tree) + '\n')
    #
    # tree.remove(7)
    # print (str(tree) + '\n')
    #
    # tree.remove(8)
    # print (str(tree) + '\n')
    #
    # tree = BST()
    # print (str(tree) + '\n')
    #
    # tree.insert(5)
    # tree.insert(3)
    # tree.insert(7)
    # tree.insert(1)
    # tree.insert(4)
    # tree.insert(6)
    # tree.insert(8)
    # tree.insert(9)
    # tree.insert(3.5)
    # print (str(tree) + '\n')
    #
    # tree.remove(3)
    # print (str(tree) + '\n')
