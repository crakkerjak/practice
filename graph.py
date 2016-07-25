#!/usr/bin/env python3

class Queue:
    def __init__(self):
        self.q = []

    def __str__(self):
        return str(self.q)

    def put(self, obj):
        self.q.append(obj)

    def get(self):
        if not self.empty():
            next_obj = self.q[0]
            self.q = self.q[1:]
            return next_obj
        return None

    def empty(self):
        return len(self.q) == 0


class Stack:
    def __init__(self):
        self.s = []

    def __str__(self):
        return str(self.s)

    def push(self, obj):
        self.s.append(obj)

    def pop(self):
        return self.s.pop()

    def empty(self):
        return len(self.s) == 0


class Node:
    def __init__(self, data=None, adj=[]):
        self.data = data
        self.adj = adj


class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def bfs(self, start, tgt):
        # uses queue, mark nodes discovered when enqueued
        if not start in self.nodes:
            return None
        # setup
        # from queue import Queue  # using homespun version
        for node in self.nodes:
            node.discovered = False
        q = Queue()
        start.discovered = True
        q.put(start)

        # search
        while not q.empty():
            current_node = q.get()
            print ('visited: ' + str(current_node.data))
            if current_node.data == tgt:
                # found -> return this node
                return current_node
            else:
                # enqueue undiscovered adjacent nodes
                for node in current_node.adj:
                    if not node.discovered:
                        node.discovered = True
                        q.put(node)
        # not found
        return None

    def dfs(self, start, tgt):
        # uses stack, mark nodes discovered when popped
        if not start in self.nodes:
            return None
        # setup
        for node in self.nodes:
            node.discovered = False
        s = Stack()
        s.push(start)

        # search
        while not s.empty():
            current_node = s.pop()
            print ('visited: ' + str(current_node.data))
            if current_node.data == tgt:
                # found -> return this node
                return current_node
            else:
                current_node.discovered = True
                for node in current_node.adj:
                    if not node.discovered:
                        s.push(node)
        # not found
        return None


if __name__ == '__main__':
    a = Node('a')
    b = Node('b', [a])
    c = Node('c', [b])
    d = Node('d', [a, c])
    e = Node('e', [b, d])
    f = Node('f', [c])
    g = Node('g', [f])

    a.adj.append(b)
    a.adj.append(d)
    b.adj.append(c)
    b.adj.append(e)
    c.adj.append(d)
    c.adj.append(f)
    d.adj.append(e)
    f.adj.append(g)

    graph = Graph([a, b, c, d, e, f, g])

    # graph = undirected (/bidirectional) graph:
    #            (d)
    #          /  |  \
    #        (a) (e) (c)-(f)-(g)
    #          \  |  /
    #            (b)

    tgt_node = graph.bfs(f, 'e')
    if tgt_node is not None:
        print('target found: {}'.format(tgt_node.data))
    else:
        print('not found')

    print()

    tgt_node = graph.dfs(f, 'a')
    if tgt_node is not None:
        print('target found: {}'.format(tgt_node.data))
    else:
        print('not found')
